#  packages required to build movie recommendation system
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity



import os

# to read dataset and retrieve information
csv_path = "tmdb_5000_movies.csv"
if not os.path.exists(csv_path):
    raise FileNotFoundError(
        f"Required dataset '{csv_path}' not found in the working directory.\n"
        "Please download 'tmdb_5000_movies.csv' and place it next to this script."
    )

movies = pd.read_csv(csv_path)

movies = movies[['title', 'overview']]
movies.dropna(inplace=True)

movies.head()



# Convert Text to Numerical Features (TF-IDF)

tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(movies['overview'])
print(tfidf_matrix.shape)


# Compute Cosine Similarity
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)
print(cosine_sim.shape)



# test the system
indices = pd.Series(movies.index, index=movies['title'])
print(indices.head())



# Create Recommendation Function
def get_recommendations(title, num_recommendations=10):
    if title not in indices:
        print(f"Movie '{title}' not found in the database. Please check the title.")
        return []

    idx = indices[title]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:num_recommendations+1]
    movie_indices = [i[0] for i in sim_scores]
    return movies['title'].iloc[movie_indices]

print("Recommendation function 'get_recommendations' defined.")



#  Call recommendation function

recommendations = get_recommendations('The Dark Knight Rises', 5)
print(f"Recommendations for 'The Dark Knight Rises':\n{recommendations}")