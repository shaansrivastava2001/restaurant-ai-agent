from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings
from langchain_core.documents import Document

import os
import pandas as pd

# load csv in a pandas dataframe
df = pd.read_csv('realistic_restaurant_reviews.csv')
embeddings = OllamaEmbeddings(model="mxbai-embed-large")

# check if db already exists
db_location = "./chroma_langchain_db"
db_exists = os.path.exists(db_location)

# if db doesn't exist, create it
if not db_exists:
    documents, ids = [], []
    for i, row in df.iterrows():
        document = Document(
            page_content = row["Title"] + " " + row["Review"],
            metadata = { "rating": row["Rating"], "date": row["Date"] },
            id = str(i)
        )
        ids.append(str(i))
        documents.append(document)

# create vector store
vector_store = Chroma(
    collection_name="restaurant_reviews",
    persist_directory=db_location,
    embedding_function=embeddings
)

# if db doesn't exist, add documents to db
if not db_exists:
    vector_store.add_documents(documents=documents, ids=ids)

# allow us to grab relevant documents
retriever = vector_store.as_retriever(search_type="similarity", search_kwargs={"k": 5})
