import pandas as pd
import numpy as np
import ast
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import streamlit as st

def convert(row):
    l=[]
    for i in ast.literal_eval(row):
        l.append(i['name'])
    return l

def collapse(l):
    l1=[]
    for i in l:
        l1.append(i.replace(' ',''))
    return l1

def convert_cast(row):
    l=[]
    counter=0
    for i in ast.literal_eval(row):
        if counter!=3:
            l.append(i['name'])
            counter+=1
        else:
            break
    return l

def convert_crew(row):
    l=[]
    for i in ast.literal_eval(row):
        if i["job"]=="Director":
            l.append(i["name"])
    return l

def recommend(movie_name):
    index=movies[movies['title']==movie_name].index[0]
    distances=sorted(list(enumerate(co_sim[index])),reverse=True,key=lambda x:x[1])
    l=[]
    for i in distances[1:6]:
        l.append(movies.iloc[i[0]].title)
    return l

movies=pd.read_csv("https://github.com/Shesh009/English_movie_Recommendation/blob/master/tmdb_5000_movies.csv")
credits=pd.read_csv("https://github.com/Shesh009/English_movie_Recommendation/blob/master/tmdb_5000_credits.csv")

data=movies.merge(credits,on="title")
data.dropna(inplace=True)
data1=data

data=data[["movie_id","title","genres","overview","keywords","cast","crew"]]

data["genres"]=data["genres"].apply(convert)
data["keywords"]=data["keywords"].apply(convert)
data.cast=data.cast.apply(convert_cast)
data.crew=data.crew.apply(convert_crew)

data['cast']=data['cast'].apply(collapse)
data['crew']=data['crew'].apply(collapse)
data['genres']=data['genres'].apply(collapse)
data['keywords']=data['keywords'].apply(collapse)

data['overview']=data['overview'].apply(lambda x:x.split())

data['all_aspects']=data['genres']+data['overview']+data['keywords']+data['cast']+data['crew']

data['all_aspects']=data['all_aspects'].apply(lambda x:" ".join(x))

movies=data[['movie_id','title','all_aspects']]
movies=movies.set_index("movie_id").reset_index()

cv=CountVectorizer(max_features=5000,stop_words='english')
count_matrix = cv.fit_transform(movies["all_aspects"])

co_sim=cosine_similarity(count_matrix)

st.title("MOVIE RECOMMENDATION SYSTEM")
mov=st.selectbox("Select a movie",movies.title)
st.subheader("MOVIE RECOMMENDATION")
st.caption("Because you watched : "+mov)
for j in range(0,5):
    st.button(recommend(mov)[j])
