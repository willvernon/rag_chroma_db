from langchain_chroma import Chroma
from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_huggingface import HuggingFaceEmbeddings
import os

# Initialize embedding function
model_path = os.path.expanduser("./sentence_transformers/all-MiniLM-L6-v2")
embedding_function = HuggingFaceEmbeddings(model_name=model_path)

# Initialize Chroma with the embedding function
vectorstore = Chroma(
    persist_directory="./chroma_db",
    collection_name="pkb_collection",
    embedding_function=embedding_function,
)
llm = ChatOllama(model="gemma3:4b")
retriever = vectorstore.as_retriever(search_kwargs={"k": 2})

# Define prompt template
template = """Context: {context}
Question: {question}
Answer: """
prompt = PromptTemplate.from_template(template)

# Create RAG chain
chain = (
    {"context": retriever, "question": RunnablePassthrough()}
    | prompt
    | llm
    | StrOutputParser()
)

# Test query
question = "What is Python used for in AI?"
result = chain.invoke(question)
print(result)
