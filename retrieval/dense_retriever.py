#dense retrieval -> finding documents based on semantic meaning
#embeddings are dense vectors
#most dimensions contain non-zero values

from vectorstore.store import query_collection

class DenseRetriever:

    #collection -> chroma collection
    #model -> SentenceTransformer

    def __init__(self , collection , model):
        self.collection = collection
        self.model = model


    def retrieve(self , query , k):

        query_embedding = self.model.encode(query).tolist()

        results = query_collection(
            self.collection,
            query_embedding,
            k
        )

        return results