import os
import pickle
from umap import UMAP
from hdbscan import HDBSCAN
from sentence_transformers import SentenceTransformer
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
from bertopic import BERTopic
from bertopic.representation import KeyBERTInspired
from bertopic.vectorizers import ClassTfidfTransformer

# Read the data from CSV file
csv_file_path = '/Users/justynakurach/Documents/GitHub/IronHackLabs/FInal Project/Ecommerce_data.csv'
df = pd.read_csv(csv_file_path)

# Check if 'Text' column is a list, if not convert it to a list
if isinstance(df['Text'], list):
    text = df['Text']
else:
    text = df['Text'].tolist()

# Initialize models for each step
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")
umap_model = UMAP(n_neighbors=10, n_components=2, min_dist=0.01, metric='cosine')
hdbscan_model = HDBSCAN(min_cluster_size=20, min_samples=1, metric='euclidean', cluster_selection_method='leaf', prediction_data=True)
vectorizer_model = CountVectorizer(ngram_range=(1, 2), stop_words="english")
ctfidf_model = ClassTfidfTransformer()
representation_model = KeyBERTInspired()

nr_topics = 50

# Create BERTopic model
model = BERTopic(
    nr_topics=nr_topics,
    language='english',
    calculate_probabilities=True,
    embedding_model=embedding_model,
    umap_model=umap_model,
    hdbscan_model=hdbscan_model,
    vectorizer_model=vectorizer_model,
    ctfidf_model=ctfidf_model,
    representation_model=representation_model,
    verbose=True
)

# Fit the model on the text data
topics, probs = model.fit_transform(text)

# Save the model, topics, and probabilities using pickle
directory = "/Users/justynakurach/Documents/"
model_path = os.path.join(directory, "bertopic_model.pkl")
topics_path = os.path.join(directory, "topics.pkl")
probs_path = os.path.join(directory, "probs.pkl")

try:
    with open(model_path, 'wb') as file:
        pickle.dump(model, file)

    with open(topics_path, 'wb') as file:
        pickle.dump(topics, file)

    with open(probs_path, 'wb') as file:
        pickle.dump(probs, file)

    print("Pickles saved successfully!")
except Exception as e:
    print(f"Error occurred while saving pickles: {str(e)}")
