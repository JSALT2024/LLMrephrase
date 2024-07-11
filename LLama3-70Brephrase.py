import json
import torch
from transformers import (AutoTokenizer,
                            AutoModelForCausalLM,
                            BitsAndBytesConfig,
                            pipeline)

HF_TOKEN = "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"

def rephrase_sentence(sentence, num):

    if num == 1:
        messages=[
        {"role": "system", "content": f"You are a helpful assistant that rephrases a given sentence. Try to be semantically consistent. Make sure the paraphrase includes all the information from the original sentence, don't output any other text."},
        {"role": "user", "content": f"{sentence}"}]
    else:
        messages=[
        {"role": "system", "content": f"You are a helpful assistant that rephrases a given sentence in {num} ways, each on its own line. Try to be semantically consistent. You don't output any other text than these sentences."},
        {"role": "user", "content": f"{sentence}"}]

    pipe.tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
    
    outputs = pipe(
        messages,
        max_new_tokens=8192,
        eos_token_id=terminators,
        do_sample=True,
        temperature=0.6,
        top_p=0.9,
        pad_token_id = pipe.tokenizer.eos_token_id)

    return outputs[0]["generated_text"][-1]["content"].split('\n')

if __name__ == "__main__":
    pipe = pipeline(
        "text-generation",
        model="meta-llama/Meta-Llama-3-70B-Instruct",
        model_kwargs={"torch_dtype": torch.bfloat16},
        device_map="auto",
        token=HF_TOKEN)

terminators = [
    pipe.tokenizer.eos_token_id,
    pipe.tokenizer.convert_tokens_to_ids("<|eot_id|>")]

with open("/auto/brno2/home/javorek/LLama3-70Brephrase_output.txt", 'a') as f:
    from datetime import datetime
    now = datetime.now()
    f.write("start date and time =", now.strftime("%d/%m/%Y %H:%M:%S"),"\n")
    f.write(rephrase_sentence("Edgar Allan Poe lived in Baltimore during the 1830s and is buried there.",5),"\n")
    now = datetime.now()
    f.write("end date and time =", now.strftime("%d/%m/%Y %H:%M:%S"),"\n")

