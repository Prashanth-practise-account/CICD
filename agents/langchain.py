from langchain_ollama import Ollama
from langchain_core.documents import Document
from langchain.tools import tool
from langchain_community.vectorstores import FAISS
from langgraph.graph import StateGraph,START, END
from Sentence_Transformers import sentence_transformers

llm = Ollama(model="mistral:latest",TimeoutError=100,max_output_token=5000,temperature=0.1)
docum = [
    Document(
        page_content="""

    """
    ),
    Document(
        page_content="""

    """
    )
]

