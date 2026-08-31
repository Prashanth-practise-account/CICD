from langchain_core.documents import Document
from langchain_ollama import Ollama

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

