## For setting up this Chroma DB you need the following:

- `pip install chromadb`
- `mkdir ~/chroma_db`

## Embeddings Function 'all-MiniLM-L6-v2'

- `python3 -m pip install sentence-transformers`

## Needed for RAG-Quary

- `python3 -m pip install langchain langchain-community langchain-ollama`

## For preprocessing text files or PDFs to remove unnecessary content you could use:

- `python3 -m pip install PyPDF2`

## Adding Documents to a collection:

- Make sure for documents to limit content to 250-500 word chunks.
- When using `add_data.py` make sure to enclose documents and ids in `" "` parenthesis.

## To Run each script:

- `ollama serve`
- `python3 rag_query.py`
