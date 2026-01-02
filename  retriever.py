from sentence_transformers import SentenceTransformer
import numpy as np

model = SentenceTransformer("paraphrase-multilingual-MiniLM-L12-v2")

def retrieve(query, index, metadata, k=3):
    q_emb = model.encode(query).astype("float32")
    distances, indices = index.search(np.array([q_emb]), k)

    results = []
    for i in indices[0]:
        results.append(metadata[i])

    return results
