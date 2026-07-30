from sentence_transformers import SentenceTransformer


def load_model(model_name):
    # returns a loaded SentenceTransformer
    model = SentenceTransformer(model_name)
    return model


def embed_chunks(model, chunks):
    #given the chunks , makes vector embeddings out of it
    return model.encode(chunks)