import faiss
import numpy as np

index = faiss.IndexFlatL2(1536)

documents = []

def add_document(embedding, doc):

    vector = np.array([embedding]).astype("float32")
    index.add(vector)

    documents.append(doc)


def search(query_embedding):

    vector = np.array([query_embedding]).astype("float32")

    distances, indices = index.search(vector, k=5)

    return [documents[i] for i in indices[0]]
