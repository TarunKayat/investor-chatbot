from ingest import load_documents
from embed_store import build_index
from retriever import retrieve
from gemini_client import model
from language import detect_language

print("📄 Loading documents...")
docs = load_documents()
index, metadata = build_index(docs)
print("✅ Ready\n")

print("🤖 Bilingual Investor Relations Chatbot (EN / JP)")
print("Type 'exit' to quit\n")

while True:
    query = input("You: ")
    if query.lower() == "exit":
        break

    lang = detect_language(query)
    chunks = retrieve(query, index, metadata)

    context = "\n".join([c["text"] for c in chunks])

    if lang == "ja":
        prompt = f"""
以下の情報を使って質問に答えてください。

情報:
{context}

質問:
{query}
"""
    else:
        prompt = f"""
Answer the question using the information below.
if not say, no information about this.

Context:
{context}

Question:
{query}
"""

    response = model.generate_content(prompt)
    print("Bot:", response.text.strip(), "\n")
