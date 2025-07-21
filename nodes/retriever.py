# retriever.py  imported by nodes
import os
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

_DB_DIR = os.path.join(os.path.dirname(__file__), "../vector_db")
embedding_model = "sentence-transformers/LaBSE"
_emb    = HuggingFaceEmbeddings(model=embedding_model)

vectordb  = Chroma(persist_directory=_DB_DIR,
                   embedding_function=_emb)
retriever = vectordb.as_retriever(search_kwargs={"k": 8})   # tune k later



# For test DELETE LATER---
if __name__ == "__main__":
    query = "ТОО   «МИДАС(HAS)» подозревается в"
    docs = retriever.get_relevant_documents(query)

    print(f"Retrieved {len(docs)} chunks for: “{query}”\n")
    for i, d in enumerate(docs, 1):
        src = d.metadata.get("source", "no‑source")
        preview = d.page_content.strip().replace("\n", " ")
        print(f"[{i}] {src}\n    {preview}…\n")