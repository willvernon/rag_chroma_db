import chromadb
from chromadb.config import Settings
from chromadb.utils import embedding_functions

user_input_path = input("What is the path to DB?: ")
user_input_collection = input("What is the collection name?: ")

# Initialize Chroma with persistent storage
client = chromadb.PersistentClient(
    path=user_input_path,
    settings=Settings(anonymized_telemetry=False),
)
ef = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name="all-MiniLM-L6-v2"
)
collection = client.create_collection(name=user_input_collection, embedding_function=ef)

print(f"Chroma Collection {user_input_collection} created with SentenceTransformer!")
