import pickle
import pandas as pd
import requests
import streamlit as st


def fetch_poster(movie_id):
    '''Function takes movie_id and returns poster link.'''

    response = requests.get('https://api.themoviedb.org/3/movie/{}?'
                            'api_key=72278677787790b080ceb7feb0a5531f'.format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']


def recommend(movie):
    '''Function takes a movie (string) and returns 10 similar movie names list and their respective posters.'''

    movie_index = movies[movies["title"] == movie].index[0]
    distance = similarity[movie_index]
    movies_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:11]
    recommended_movies = []
    recommended_movies_posters = []

    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies, recommended_movies_posters


file_path = 'movie_list.pkl'

with open(file_path, 'rb') as file:
    movies_dict = pickle.load(file)

file_p = 'similarity.pkl'
with open(file_p, 'rb') as file:
    similarity = pickle.load(file)

movies = pd.DataFrame(movies_dict)

st.title("Movie Recommender System ")

selected_movie_name = st.selectbox(
    'Select a Movie🍿',
    movies['title'].values)

if st.button('Recommend'):
    names, posters = recommend(selected_movie_name)

    col1, col2, col3, col4, col5 = st.columns(5, gap="medium")

    with col1:
        st.image(posters[0])
        st.caption(names[0])

    with col2:
        st.image(posters[1])
        st.caption(names[1])

    with col3:
        st.image(posters[2])
        st.caption(names[2])

    with col4:
        st.image(posters[3])
        st.caption(names[3])

    with col5:
        st.image(posters[4])
        st.caption(names[4])

    col6, col7, col8, col9, col10 = st.columns(5, gap="medium")

    with col6:
        st.image(posters[5])
        st.caption(names[5])

    with col7:
        st.image(posters[6])
        st.caption(names[6])

    with col8:
        st.image(posters[7])
        st.caption(names[7])

    with col9:
        st.image(posters[8])
        st.caption(names[8])

    with col10:
        st.image(posters[9])
        st.caption(names[9])