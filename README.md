# LLMrephrase
Text enrichment (paraphrasing/rephrasing) of sign language datasets [How2Sign](https://how2sign.github.io/) and [YoutubeASL](https://arxiv.org/abs/2306.15162) using GPT-3.5/4o/4o-mini, Llama3-8B, Llama3-70B, Claude3.5, Gemini.

Code repository affiliated with the SignLLaVa team at the [JSALT 2024](https://www.clsp.jhu.edu/2024-tenth-jelinek-summer-workshop-on-speech-and-language-technology-schedule/) workshop.

## Structure

 - [paraphrase_scripts](https://github.com/JSALT2024/LLMrephrase/tree/main/paraphrase_scripts "paraphrase_scripts") - core scripts for paraphrasing by [**Václav Javorek**](https://github.com/VaJavorek)
	 - [LLMrephrase.ipynb](https://github.com/JSALT2024/LLMrephrase/blob/main/paraphrase_scripts/LLMrephrase.ipynb "LLMrephrase.ipynb") - concept proof code + dataset statistics
	 - [GPTrephrase.ipynb](https://github.com/JSALT2024/LLMrephrase/blob/main/paraphrase_scripts/GPTrephrase.ipynb "GPTrephrase.ipynb") - core script using GPT API
	 - [GPTrephrase_4o-mini.ipynb](https://github.com/JSALT2024/LLMrephrase/blob/main/paraphrase_scripts/GPTrephrase_4o-mini.ipynb "GPTrephrase_4o-mini.ipynb") - 4o-mini version
	 - [GPTrephrase_H2S.ipynb](https://github.com/JSALT2024/LLMrephrase/blob/main/paraphrase_scripts/GPTrephrase_H2S.ipynb "GPTrephrase_H2S.ipynb") - How2Sign version
	 - [GPTrephrase_H2S_4o-mini.ipynb](https://github.com/JSALT2024/LLMrephrase/blob/main/paraphrase_scripts/GPTrephrase_H2S_4o-mini.ipynb "GPTrephrase_H2S_4o-mini.ipynb") - 4o-mini  How2Sign
	 - [Llama3rephrase.ipynb](https://github.com/JSALT2024/LLMrephrase/blob/main/paraphrase_scripts/Llama3rephrase.ipynb "Llama3rephrase.ipynb") - Llama3 (8B) version
	 - [Llama3rephrase+context.ipynb](https://github.com/JSALT2024/LLMrephrase/blob/main/paraphrase_scripts/Llama3rephrase%2Bcontext.ipynb "Llama3rephrase+context.ipynb") - Contextual paraphrasing
	 - [Llama3rephrase+context-iter.ipynb](https://github.com/JSALT2024/LLMrephrase/blob/main/paraphrase_scripts/Llama3rephrase%2Bcontext-iter.ipynb "Llama3rephrase+context-iter.ipynb") - Iterative rephrasing
	 - [Llama3rephrase_HF.ipynb](https://github.com/JSALT2024/LLMrephrase/blob/main/paraphrase_scripts/Llama3rephrase_HF.ipynb "Llama3rephrase_HF.ipynb") - HuggingFace API version
	 - [error counter.ipynb](https://github.com/JSALT2024/LLMrephrase/blob/main/paraphrase_scripts/error%20counter.ipynb "error counter.ipynb") - fast bugfix and verification scripts
	 - [LLama3-70B](https://github.com/JSALT2024/LLMrephrase/tree/main/paraphrase_scripts/LLama3-70B "LLama3-70B") - scripts for rephrasing with Llama3-70B

 
 - [paraphrase_evaluation_analysis](https://github.com/JSALT2024/LLMrephrase/tree/main/paraphrase_evaluation_analysis "paraphrase_evaluation_analysis") - evaluation scripts by [**Alessa Carbo**](https://github.com/AlessaC14)
 
 - [data-normalization](https://github.com/JSALT2024/LLMrephrase/tree/main/data-normalization "data-normalization") - text preprocessing by [**Alessa**](https://github.com/AlessaC14)  and [**Dominik**](https://github.com/Gldkslfmsd)
 
 - [keywords](https://github.com/JSALT2024/LLMrephrase/tree/main/keywords "keywords"), [text-distance](https://github.com/JSALT2024/LLMrephrase/tree/main/text-distance "text-distance") - multitask and utility scripts by [**Dominik Macháček**](https://github.com/Gldkslfmsd)

Note: All HF and OpenAI tokens contained within code repository are legacy and were generated and used solely for JSALT2024 purposes.