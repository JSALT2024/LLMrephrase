import os
import sys
from lang_id import identify_language
from true_case import apply_truecasing
import re

def log(message):
    print(message, flush=True)

def remove_special_characters(text):
    pattern = r'[♪♫🎵🎶\U0001F3B5\U0001F3B6\U0001F3BC]'  # Music notes and symbols
    pattern += r'|[\U0001F600-\U0001F64F]'  # Emoticons
    pattern += r'|[\U0001F300-\U0001F5FF]'  # Symbols & Pictographs
    pattern += r'|[\U0001F680-\U0001F6FF]'  # Transport & Map Symbols
    pattern += r'|[\U0001F1E0-\U0001F1FF]'  # Flags (iOS)
    pattern += r'|[\U00002702-\U000027B0]'
    pattern += r'|[\U000024C2-\U0001F251]'
    pattern += r'|[\U0001f926-\U0001f937]'
    pattern += r'|[\U00010000-\U0010ffff]'
    pattern += r'|[\u2600-\u26FF\u2700-\u27BF]'  # Dingbats
    pattern += r'|@'  # Remove @ symbol
    return re.sub(pattern, '', text)

def normalize_text(text):
    text = text.lower()
    text = remove_special_characters(text)
    
    # Remove spaces inside quotation marks
    text = re.sub(r'"\s+(.+?)\s+"', r'"\1"', text)
    
    text = re.sub(r'\s+', ' ', text)
    text = text.strip()
    text = re.sub(r'\s([,.!?;:](?:\s|$))', r'\1', text)
    return text



def filter_short_sentences(text, min_length=4):
    sentences = re.split(r'(?<=[.!?])\s+', text)
    filtered_sentences = [s for s in sentences if len(s.strip()) >= min_length]
    return ' '.join(filtered_sentences)

def process_text(text):
    text = normalize_text(text)
    text = filter_short_sentences(text)
    return text.strip()

def run_clean_mono(input_file, output_file, num_fields):
    log(f"Starting text normalization for {input_file}")
    try:
        with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
            for line in infile:
                fields = line.strip().split('\t')
                if len(fields) == num_fields:
                    processed_text = process_text(fields[-1])
                    if processed_text:  # Only write if there's text left after processing
                        fields[-1] = processed_text
                        outfile.write('\t'.join(fields) + '\n')
                else:
                    outfile.write(line)
        log(f"Completed text normalization for {input_file}")
    except Exception as e:
        log(f"Error in text normalization: {e}")
        raise

def apply_truecasing_to_file(input_file, output_file):
    log(f"Starting truecasing for {input_file}")
    try:
        with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
            for line in infile:
                fields = line.strip().split('\t')
                fields[-1] = apply_truecasing(fields[-1])
                outfile.write('\t'.join(fields) + '\n')
        log(f"Completed truecasing for {input_file}")
    except Exception as e:
        log(f"Error applying truecasing: {e}")
        raise

def apply_lang_id_to_file(input_file, output_file):
    log(f"Starting language identification for {input_file}")
    try:
        with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
            for line in infile:
                fields = line.strip().split('\t')
                lang = identify_language(fields[-1])
                outfile.write(f"{lang}\t{line.strip()}\n")
        log(f"Completed language identification for {input_file}")
    except Exception as e:
        log(f"Error applying language identification: {e}")
        raise

def process_file(input_file, output_file, num_fields):
    log(f"Starting processing for {input_file}")
    temp_file1 = f"{output_file}.temp1"
    temp_file2 = f"{output_file}.temp2"

    try:
        run_clean_mono(input_file, temp_file1, num_fields)
        apply_truecasing_to_file(temp_file1, temp_file2)
        apply_lang_id_to_file(temp_file2, output_file)
        log(f"Completed processing for {input_file}")
    except Exception as e:
        log(f"Error in process_file for {input_file}: {e}")
        raise
    finally:
        for file in [temp_file1, temp_file2]:
            if os.path.exists(file):
                os.remove(file)
                log(f"Removed temporary file: {file}")

def main():
    main_file = "train.filtered3.beg_dur_id_frames_fps_text.tsv"
    alignment_file = "train.filtered3.beg_dur_id_text.tsv"

    main_output = "train.filtered3.beg_dur_id_frames_fps_text.processed.tsv"
    alignment_output = "train.filtered3.beg_dur_id_text.processed.tsv"

    try:
        log("Starting main file processing")
        process_file(main_file, main_output, 6)
        log("Completed main file processing")

        log("Starting alignment file processing")
        process_file(alignment_file, alignment_output, 4)
        log("Completed alignment file processing")

        log(f"Processing complete. Output files:")
        log(f"1. Main file: {main_output}")
        log(f"2. Alignment file: {alignment_output}")
    except Exception as e:
        log(f"An error occurred in main: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()

