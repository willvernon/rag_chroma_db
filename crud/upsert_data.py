# update or insert if does not exist
import chromadb
from chromadb.utils import embedding_functions

user_input_collection = input("Add to what Collection: ")
user_input_docs = input("Path to Document in Quotes: ")
# Docs need to be in " "
user_input_id = input("Give Document ID in Quotes: ")
# IDs need to be in " "

client = chromadb.PersistentClient(path="./chroma_db")
ef = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name="all-MiniLM-L6-v2"
)
collection = client.get_collection(name=user_input_collection, embedding_function=ef)

collection.upsert(ids=user_input_id, documents=user_input_docs)

print("Documents Updated/Inserted")
