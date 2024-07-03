import pandas as pd
import torch
from bert_score import BERTScorer
from tqdm import tqdm


df = pd.read_csv('rephrased_3100-33599.csv')


scorer = BERTScorer(lang="en", rescale_with_baseline=True)


def calculate_bert_score(row):
    caption = str(row['Caption'])
    scores = []
    for i in range(1, 6):
        rephrase_key = f'GPT_Rephrase{i}'
        if rephrase_key in row and pd.notna(row[rephrase_key]):
            rephrase = str(row[rephrase_key])  
            try:
                _, _, f1 = scorer.score([rephrase], [caption])
                scores.append(f1.item())
            except Exception as e:
                print(f"Error processing row {row.name}, rephrase {i}: {e}")
                print(f"Caption: {caption}")
                print(f"Rephrase: {rephrase}")
    return scores if scores else None

# Calculate BERT Scores for rows 3100 to 33599 (rephrase rows in this sample)
results = []
for index, row in tqdm(df.iloc[3100:33600].iterrows(), total=30500):
    try:
        scores = calculate_bert_score(row)
        if scores:
            results.append({
                'ClipID': row['ClipID'],
                'Caption': row['Caption'],
                'BERT_Scores': scores,
                'Avg_BERT_Score': sum(scores) / len(scores)
            })
    except Exception as e:
        print(f"Error processing row {index}: {e}")


results_df = pd.DataFrame(results)


results_df.to_csv('bert_score_results.csv', index=False)

print("BERT Score evaluation completed. Results saved to 'bert_score_results.csv'.")