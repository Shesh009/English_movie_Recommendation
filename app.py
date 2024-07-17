import pandas as pd
import numpy as np
import ast
import sklearn
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import streamlit as st

# Function to convert stringified lists into a list of names
def convert(row):
    l = []
    for i in ast.literal_eval(row):
        l.append(i['name'])
    return l

# Function to remove spaces in names for uniformity
def collapse(l):
    l1 = []
    for i in l:
        l1.append(i.replace(' ', ''))
    return l1

# Function to extract the first 3 cast members
def convert_cast(row):
    l = []
    counter = 0
    for i in ast.literal_eval(row):
        if counter != 3:
            l.append(i['name'])
            counter += 1
        else:
            break
    return l

# Function to extract the director's name
def convert_crew(row):
    l = []
    for i in ast.literal_eval(row):
        if i["job"] == "Director":
            l.append(i["name"])
    return l

# Function to recommend movies based on cosine similarity
def recommend(movie_name):
    try:
        index = movies[movies['title'] == movie_name].index[0]
        distances = sorted(list(enumerate(co_sim[index])), reverse=True, key=lambda x: x[1])
        l = []
        for i in distances[1:6]:
            l.append(movies.iloc[i[0]].title)
        return l
    except IndexError:
        return []

# Load datasets
movies = pd.read_csv("tmdb_5000_movies.csv")
credits = pd.read_csv("tmdb_5000_credits.csv")

# Merge datasets on title
data = movies.merge(credits, on="title")
data.dropna(inplace=True)

# Select relevant columns
data = data[["movie_id", "title", "genres", "overview", "keywords", "cast", "crew"]]

# Apply conversion functions
data["genres"] = data["genres"].apply(convert)
data["keywords"] = data["keywords"].apply(convert)
data["cast"] = data["cast"].apply(convert_cast)
data["crew"] = data["crew"].apply(convert_crew)

# Collapse names for uniformity
data['cast'] = data['cast'].apply(collapse)
data['crew'] = data['crew'].apply(collapse)
data['genres'] = data['genres'].apply(collapse)
data['keywords'] = data['keywords'].apply(collapse)

# Split overview into words
data['overview'] = data['overview'].apply(lambda x: x.split())

# Combine all aspects into a single string
data['all_aspects'] = data['genres'] + data['overview'] + data['keywords'] + data['cast'] + data['crew']
data['all_aspects'] = data['all_aspects'].apply(lambda x: " ".join(x))

# Create a new DataFrame with movie_id, title, and all_aspects
movies = data[['movie_id', 'title', 'all_aspects']]
movies = movies.set_index("movie_id").reset_index()

# Create the count matrix and cosine similarity matrix
cv = CountVectorizer(max_features=5000, stop_words='english')
count_matrix = cv.fit_transform(movies["all_aspects"])

co_sim = cosine_similarity(count_matrix)

# Streamlit app
st.title("MOVIE RECOMMENDATION SYSTEM")
mov = st.selectbox("Select a movie", movies.title)
st.subheader("MOVIE RECOMMENDATION")
st.caption("Because you watched : " + mov)

recommendations = recommend(mov)
for rec in recommendations:
    st.button(rec)
