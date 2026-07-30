#chromaDB is a vector database that creates a smaller subset of data of its own and makes a neighbourhood.
#it kind of creates an index on the database
import chromadb
from sentence_transformers import SentenceTransformer


#collection is a container that stores related vectors and associated data



def get_collection(name="data"):
    # creates a client
    client = chromadb.Client()
    collection = client.get_or_create_collection(name=name)

    return collection





def add_to_collection(collection, chunks, embeddings, ids):

    collection.add(
        documents=chunks,
        embeddings=embeddings,
        ids = ids
    )





def query_collection(collection, query_embedding, n_results=2):
    #query on a specific collection
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=n_results
    )

    return results




# chunks = [
#     "my name is agastya",
#     "im a boy",
#     "im 19 years old",
#     "agastya is a hardworking guy"
# ]

# model = SentenceTransformer('all-MiniLM-L6-v2')

# result = model.encode(chunks)

# client = chromadb.Client()

# collection = client.create_collection("data")

# collection.add(
#     documents=chunks,
#     embeddings=result,
#     ids = ["1" , "2" , "3" , "4"]
# )


# query = "how old is agastya"
# query_embedding = model.encode(query).tolist()

# results = collection.query(
#     query_embeddings=[query_embedding],
#     n_results=2
# )

# print(results)