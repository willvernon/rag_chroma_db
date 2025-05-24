from datetime import datetime

import chromadb
from chromadb.utils import embedding_functions

# Collections have a few useful convenience methods.
#
#     collections.peek() - returns a list of the first 10 items in the collection.
#                .count() - returns the number of items in the collection.
#                .modify(name="new_name") - rename the collection

client = chromadb.PersistentClient(path="./chroma_db")
ef = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name="all-MiniLM-L6-v2"
)
user_input = input("Collection Name: ")
user_input_2 = input("Collection Description: ")
collection = client.create_collection(
    name=user_input,
    embedding_function=ef,
    metadata={"description": user_input_2, "created": str(datetime.now())},
)
