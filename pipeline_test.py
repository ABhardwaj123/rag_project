from ingestion.chunking import fixed_chunk
from embeddings.embedder import load_model, embed_chunks
from vectorstore.store import get_collection, add_to_collection, query_collection
from config import CHUNK_SIZE, OVERLAP, EMBEDDING_MODEL_NAME, COLLECTION_NAME, N_RESULTS
from generation.answer import generate_answer


text = """
Agastya is a 19-year-old student currently pursuing his undergraduate degree in Computer Science at MIT Manipal. He is particularly interested in the fields of artificial intelligence and machine learning, and has been spending a lot of his free time building small projects to understand how large language models work under the hood.

In his free time, Agastya enjoys playing badminton and going for long walks around campus. He recently picked up chess again after a few years away from the game, and has been playing casual matches with friends in his hostel almost every evening. He also enjoys watching cricket matches, especially when India is playing.

Agastya's long-term career goal is to work as a machine learning engineer at a top technology company. He is especially drawn to roles involving natural language processing and retrieval-augmented generation systems, and hopes to eventually contribute to open-source AI tooling. He plans to apply for internships in this space over the next year.

Agastya was born and raised in Greater Noida, a city near Delhi, India. His family still lives there, and he tries to visit them every few months during semester breaks. He has one younger sister who is currently in high school. He describes his hometown as quiet but says he misses the food and the familiarity of home while living away for college.
"""

chunks = fixed_chunk(text , CHUNK_SIZE , OVERLAP)


model = load_model(EMBEDDING_MODEL_NAME)
embeddings = embed_chunks(model , chunks)


collection = get_collection(COLLECTION_NAME)
ids = [str(i) for i in range(len(chunks))]
add_to_collection(collection , chunks , embeddings , ids)


query = "What does Agastya want to do for his career?"
query_embedding = model.encode(query).tolist()
results = query_collection(collection , query_embedding , N_RESULTS)


retreived_chunks = results['documents'][0]
answer = generate_answer(query , retreived_chunks)

print(answer)