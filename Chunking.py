from DocumentLoader.DocumentLoader import loader
from langchain_community.vectorstores import FAISS
from langchian_text_splitter import RecursiveCharacterTextSplitter
from sentence_transformers import SentenceTransformer
from sklearn.feature_extraction.text import TfidfVectorizer


class Chunking:
    def __init__(self):
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200,
            separators=["\n\n", "\n", " ", ""]
        )
        self.embedding_model = SentenceTransformer('all-MiniLM-L6-v2')
        self.semantic_weight = 0.70
        self.keyword_weight = 0.30

    def chunk_and_embed(self):
        document_text = loader()
        self.vectors = FAISS.from_texts(
            self.text_splitter.split_text(document_text),embedding=self.embedding_model
        )

        keyward_vector = TfidfVectorizer()
        self.vectors_keyword = keyward_vector.fit_transform(self.text_splitter.split_text(document_text))

    def hybrid_search(self,query,top_k=5):
        query_embedding = self.embedding_model.encode(
            [query],
            normalize_embeddings=True
        )
        semantix_search =  self.vectors.semantic_search(query_embedding)

        query_vector = self.vectors_keyword.transform([query])
        scores = (self.vectors_keyword @ query_vector.T).toarray().flatten()

        
        hybrid_score = (
            self.keyword_weight * scores + self.semantic_weight * semantix_search
        )
        sorted_scores = sorted(hybrid_score)
        return sorted_scores[:top_k]