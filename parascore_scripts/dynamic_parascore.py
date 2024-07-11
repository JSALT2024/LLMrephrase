import pandas as pd
import numpy as np
import argparse
from transformers import AutoTokenizer, AutoModel
import torch
from scipy.spatial.distance import cosine
from Levenshtein import distance as levenshtein_distance
import os

# Load pre-trained model and tokenizer
tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
model = AutoModel.from_pretrained("bert-base-uncased")

# Move model to GPU if using
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = model.to(device)

def get_bert_embedding(text):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=512, padding=True).to(device)
    with torch.no_grad():
        outputs = model(**inputs)
    return outputs.last_hidden_state.mean(dim=1).squeeze().cpu().numpy()

def sim(text1, text2):
    emb1 = get_bert_embedding(text1)
    emb2 = get_bert_embedding(text2)
    return 1 - cosine(emb1, emb2)

def normalized_edit_distance(s1, s2):
    return levenshtein_distance(s1, s2) / max(len(s1), len(s2))

def ds(x, c, gamma=0.35):
    d = normalized_edit_distance(x, c)
    if d > gamma:
        return gamma
    return d * ((gamma + 1) / gamma) - 1

def parascore(x, c, r=None, omega=0.5):
    if r is None:
        similarity = sim(x, c)
    else:
        similarity = max(sim(x, c), sim(r, c))
    divergence = ds(x, c)
    score = similarity + omega * divergence
    return score / 1.175  # Normalize by the maximum possible score

def process_batch(batch, rephrase_columns):
    results = []
    for _, row in batch.iterrows():
        scores = []
        for col in rephrase_columns:
            if row[col] != '<none>' and pd.notna(row[col]):
                score = parascore(row['Caption'], row[col])
                scores.append(score)
            else:
                scores.append(np.nan)
        
        results.append({
            'ClipID': row['ClipID'],
            'Caption': row['Caption'],
            **{f'ParaScore_{col}': score for col, score in zip(rephrase_columns, scores)},
            'Avg_ParaScore': np.nanmean(scores)
        })
    return results

def process_csv(file_path, batch_size=1000):
    df = pd.read_csv(file_path)
    
    # Identify rephrase columns dynamically
    rephrase_columns = [col for col in df.columns if "Rephrase" in col]
    
    results = []
    for i in range(0, len(df), batch_size):
        batch = df.iloc[i:i+batch_size]
        batch_results = process_batch(batch, rephrase_columns)
        results.extend(batch_results)
        print(f"Processed batch {i//batch_size + 1}/{(len(df)-1)//batch_size + 1}")
    
    results_df = pd.DataFrame(results)
    output_filename = os.path.splitext(os.path.basename(file_path))[0] + '_parascore_results.csv'
    results_df.to_csv(output_filename, index=False)
    print(f"Processed {file_path}, results saved to {output_filename}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process a CSV file.")
    parser.add_argument("csv_file", type=str, help="Path to the CSV file to process")
    parser.add_argument("--batch_size", type=int, default=1000, help="Batch size for processing")
    args = parser.parse_args()
    process_csv(args.csv_file, args.batch_size)
