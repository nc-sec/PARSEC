# P.A.R.S.E.C. - PDF Analysis and Review System for Exam Content

This Jupyter Notebook aims to provide a system for analyzing and reviewing PDF documents related to exam content. The notebook will include various functionalities such as parsing PDF files, extracting text and metadata, performing text analysis, generating visualizations, and facilitating the review process. The goal is to create an efficient and comprehensive system for working with exam-related PDF documents.

## Intent
- This is not meant to replace a thorough understanding of the materials pertaining to your exam(s)
- It is meant to be a study & exam aid but if you don't review/tune the generated materials you're gonna have a bad time. i.e. If you don't know the exam materials you will fail.
- Don't accidentally violate copyrights/policies (and if you are/do and get caught, do the needfull & ask for forgiveness)

## stuff to fix
- if a page # contains letters, make it a topic, and also delete that page # string.. (oops)
- normalization of topics (lowercase etc)
- deduplication - identify acronyms and map to other topics
- deduplication - of topics across books
- fuzzy Grouping of topics (acronyms vs full text?) - potential alternative to alphabetical order
## Topics to explore
- More traditional/hybrid search (bm25)
- Text Embeddings & distance/cosine similarity based search (instead of text expansion)
- category-wise Grouping of topics for final 
- re-ranking (of docs after retrieval)
- An end to end implementation w/ langchain.. llama-index
- pydantic for forcing formatted outputs? or dspy
## Requirements
### Non-local 
- python
- Elastic (cloud) instance w/ ELSER Model
- OAI/Groq/Anthropic/etc. llm api key (consider privacy/policy when selecting a provider) 

### Local 
- python
- **FAISS**/weaviate/chroma/qdrant/**milvus**/**pgvector**/**elastic**/etc. (open source vector stores)
- GPU (**nvidia**, 8gb+) - I am not exploring CPU inference for llm's but you can if you like
- ollama or similar llm server/proxy (check **llama.cpp github** for a complete list)
- quantized llama3-8b or similar model

# Choosing a llm
- Local or remote
  - It's your data (probably?), you should know how to handle it
- Base or Chat versions
  - Either works, just cater your prompt to the circumstance. Experiment before batching.
- Model Size
  - You don't need a big model to do simple tasks like summarize documents (but they likely won't hurt)
  - An unquantized model is going to require a tad over 2gb of VRAM per 1b parameters (bfloat16 == 16bit)
  - Quantized versions come in all varieties and I'd recommend using one
  - 4 bit quants are common on Huggingface & provide a good tradeoff point (resource/performance)
  - Rent/test on the cloud before you buy a gpu for local LLM stuff
  
# Optional
- Langsmith Account/API key (free tier)
