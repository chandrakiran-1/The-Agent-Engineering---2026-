from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Load model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Sentences
sentence1 = "I love Python"
sentence2 = "Python is my favorite programming language"

# Create embeddings
embedding1 = model.encode(sentence1)
embedding2 = model.encode(sentence2)

# Calculate cosine similarity
score = cosine_similarity([embedding1], [embedding2])

print("Sentence 1:", sentence1)
print("Sentence 2:", sentence2)
print("Cosine Similarity:", score[0][0])