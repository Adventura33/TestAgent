# The script for indexing documents in vector DB. RUN Separetely
import glob, os, pickle
from langchain_community.document_loaders import PyPDFLoader, UnstructuredFileLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma  # FAISS
# from langchain_unstructured import UnstructuredLoader                 

DOC_DIR = "legal_docs"        
DB_DIR  = "vector_db"

def load_docs():
    for f in glob.glob(os.path.join(DOC_DIR, "*")):
        if f.lower().endswith(".pdf"):
            yield from PyPDFLoader(f).load()
        else:
            yield from UnstructuredFileLoader(f, autodetect_encoding=True).load()

docs = list(load_docs())
splitter = RecursiveCharacterTextSplitter(chunk_size=800, chunk_overlap=120)
chunks  = splitter.split_documents(docs)

embedding_model = "sentence-transformers/LaBSE"
emb = HuggingFaceEmbeddings(model_name=embedding_model)
vectordb = Chroma.from_documents(chunks, emb, persist_directory=DB_DIR)
vectordb.persist()
print(f"✅ Indexed {len(chunks):,} chunks into {DB_DIR}")
