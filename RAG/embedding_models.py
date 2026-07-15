from sentence_transformers import SentenceTransformer

# Load the embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Generate an embedding
embedding = model.encode("I love Python")

print(type(embedding))
print(len(embedding))
print(embedding[:10])  # Show first 10 values