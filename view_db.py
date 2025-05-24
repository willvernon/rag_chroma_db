import chromadb
import pandas as pd

user_input = input("View DB: ")

# Connect to the database
client = chromadb.PersistentClient(path="./chroma_db")
collection = client.get_collection(user_input)

# Fetch all data
data = collection.get(include=["documents", "metadatas"])

# Convert to DataFrame for easy viewing
df = pd.DataFrame(
    {"ID": data["ids"], "Document": data["documents"], "Metadata": data["metadatas"]}
)
print(df)
