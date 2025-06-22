from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
from langchain.schema import HumanMessage, AIMessage
from langchain.prompts import ChatPromptTemplate
from langchain.chains import RetrievalQA
import os
#os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2" 
#import os
load_dotenv()
llm=ChatGoogleGenerativeAI(model='gemini-1.5-flash')
embeddings=HuggingFaceEmbeddings(model_name='sentence-transformers/paraphrase-MiniLM-L6-v2')
path='./vectorstore'
vectorstore = FAISS.load_local(path, embeddings, allow_dangerous_deserialization=True)

#print(vectorstore)
def get_rag_response(query):
    retriever = vectorstore.as_retriever()
    qa = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)
    response = qa.invoke(query)

    # Return only the answer string, not the full dictionary
    return response.get("result") or response.get("answer") or str(response)

    

# response=get_rag_response('what is cancer')
# print(response)