import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from wordcloud import WordCloud
import seaborn as sns
np.set_printoptions(threshold=np.inf)


df = pd.read_csv('tmdb_moviescsvconvert.csv')
# Define a function to handle parsing JSON or lists
def parse_json_or_list(value):
    try:
        # Attempt to parse as JSON
        return json.loads(value)  # Try to parse the input 'value' as JSON using the json.loads() function.
    except (TypeError, ValueError):
        # If it's not valid JSON, assume it's a list (e.g., genres or keywords column)
        return eval(value)  # If parsing as JSON raises an error, assume 'value' is a list-like structure (eval() is used here, which can evaluate Python expressions).



# Apply the function to 'genres' and 'keywords' columns
df['genres'] = df['genres'].apply(parse_json_or_list)  # Apply the 'parse_json_or_list' function to the 'genres' column, which contains JSON or list data. This function parses JSON or assumes it's a list.
df['keywords'] = df['keywords'].apply(parse_json_or_list)  # Apply the 'parse_json_or_list' function to the 'keywords' column, which also contains JSON or list data.

# Define a function to create a combined string of genres and keywords
def genres_and_keywords_to_string(row):
    # Access the 'genres' and 'keywords' columns from the input 'row'
    genres = row['genres']
    keywords = row['keywords']

    # Extract and join the names of genres and keywords into separate strings
    genres_str = ' '.join(''.join(j['name'].split()) for j in genres)
    keywords_str = ' '.join(''.join(j['name'].split()) for j in keywords)

    # Combine genres and keywords into a single string, separating them with a space
    return f"{genres_str} {keywords_str}"


# Apply the function to each row of the DataFrame and store the result in a new column 'string'
df['string'] = df.apply(genres_and_keywords_to_string, axis=1)




# Initialize the TF-IDF vectorizer with a specified maximum number of features
tfidf = TfidfVectorizer(max_features=2000)
X = tfidf.fit_transform(df['string'])
print(X)

title_to_index = pd.Series(df.index, index=df['title'].str.lower())

# print(X)
# print(tfidf.vocabulary_)


# Define a function to recommend movies based on a given title
def recommend(title_data):
    lis = []
    # Get the index of the input movie title
    for i in title_data:
        movie_id = title_to_index[i.lower()]
        lis.append(X[movie_id])

    # Extract the TF-IDF vector for the input movie
    result = sum(lis)/len(title_data)
    # print(result.toarray())
    # print("-"*50)
    # print(X.toarray())

    # Calculate cosine similarities between the input movie and all movies
    scores = cosine_similarity(result, X)
    print(scores)
    print("-"*50)
    # Flatten the similarity scores
    scores = scores.flatten()
    print(scores)

    # Sort indices by descending similarity scores (excluding the input movie itself)
    recommended_movie_id = (-scores).argsort()[len(title_data):10+len(title_data)]
    print(recommended_movie_id)
    # Return the titles of the top 10 recommended movies
    return df['title'].iloc[recommended_movie_id]

