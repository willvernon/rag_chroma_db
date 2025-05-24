import streamlit as st
import chromadb

user_input = input("View DB: ")
client = chromadb.PersistentClient(path="./chroma_db")
collection = client.get_collection(user_input)

st.title("Chroma Database Viewer")
data = collection.get()
st.write("Collection Contents", data)
