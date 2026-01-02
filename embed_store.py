from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

model = SentenceTransformer("paraphrase-multilingual-MiniLM-L12-v2")

def chunk_text(text, size=500):
    return [text[i:i+size] for i in range(0, len(text), size)]

def build_index(docs):
    embeddings = []
    metadata = []

    for doc in docs:
        chunks = chunk_text(doc["text"])
        for chunk in chunks:
            emb = model.encode(chunk)
            embeddings.append(emb)
            metadata.append({
                "text": chunk,
                "language": doc["language"],
                "source": doc["source"]
            })

    dim = len(embeddings[0])
    index = faiss.IndexFlatL2(dim)
    index.add(np.array(embeddings).astype("float32"))

    return index, metadata
