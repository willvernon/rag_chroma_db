import chromadb

user_input = input("Delete Which Collection:")

client = chromadb.PersistentClient(path="./chroma_db/")
client.delete_collection(name=user_input)
print(f"Collection deleted! {user_input}")
