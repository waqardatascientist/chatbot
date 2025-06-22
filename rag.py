from dotenv import load_dotenv
from langchain.document_loaders import TextLoader,PyPDFLoader
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.text_splitter import CharacterTextSplitter,RecursiveCharacterTextSplitter
from langchain.chains import RetrievalQA
from langchain_google_genai import ChatGoogleGenerativeAI
load_dotenv()
model=ChatGoogleGenerativeAI(model='gemini-1.5-flash')
embeddings=HuggingFaceEmbeddings(model_name='sentence-transformers/paraphrase-MiniLM-L6-v2')
path='./vectorstore'
file_path='abc.pdf'
loader=PyPDFLoader(file_path)
load=loader.load()
#print(load)
spliter=RecursiveCharacterTextSplitter(chunk_size=1000,chunk_overlap=100,separators=["\n\n", "\n", " ", ""])
split=spliter.split_documents(load)
#print(split[0])
#creating vector store
vectorstore=FAISS.from_documents(split,embeddings)
save=vectorstore.save_local(path)

