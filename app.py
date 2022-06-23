import streamlit as st
import pickle
import requests

def fetch_data(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=95a03a8b56ff378521399d36656e8954&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    return data

def fetch_poster(x):
    data = fetch_data(x)
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def fetch_overview(y):
    data = fetch_data(y)
    movie_overview = data['overview']
    return movie_overview

def recommend(movie):
    index = movies[movies['movie_title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    recommended_movie_overview = []
    recommended_movie_dnames = []
    recommended_movie_genres = []
    for i in distances[0:9]:
        # fetch the movie poster
        mid = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(mid))
        recommended_movie_overview.append(fetch_overview(mid))
        recommended_movie_names.append(movies.iloc[i[0]].movie_title)
        recommended_movie_dnames.append(movies.iloc[i[0]].director_name)
        recommended_movie_genres.append(movies.iloc[i[0]].genres)

    return recommended_movie_names,recommended_movie_posters, recommended_movie_overview, recommended_movie_genres, recommended_movie_dnames

st.header('MovieFlex')
movies = pickle.load(open('model/movie_list.pkl','rb'))
similarity = pickle.load(open('model/similarity.pkl','rb'))

movie_list = movies['movie_title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

if st.button('Show Recommendation'):
    recommended_movie_names,recommended_movie_posters, recommended_movie_overview, recommended_movie_genres, recommended_movie_dnames = recommend(selected_movie)
    col0, col1 = st.columns([1, 2])
    with col0:       
        st.image(recommended_movie_posters[0], width=170)

    with col1:       
        st.header(recommended_movie_names[0])
        st.write("Overview :", recommended_movie_overview[0])
        st.write("Director name :", recommended_movie_dnames[0])
        st.write("Genres :", recommended_movie_genres[0])

    col2, col3, col4, col5 = st.columns(4)
    
    with col2:
        st.image(recommended_movie_posters[1], use_column_width='always')
        st.text(recommended_movie_names[1])

    with col3:
        st.image(recommended_movie_posters[2], use_column_width='always')
        st.text(recommended_movie_names[2])

    with col4:
        st.image(recommended_movie_posters[3], use_column_width='always')
        st.text(recommended_movie_names[3])

    with col5:       
        st.image(recommended_movie_posters[4], use_column_width='always')
        st.text(recommended_movie_names[4])

    col6, col7, col8, col9 = st.columns(4)
    with col6:
        st.image(recommended_movie_posters[5], use_column_width='always')
        st.text(recommended_movie_names[5])
    with col7:
        st.image(recommended_movie_posters[6], use_column_width='always')
        st.text(recommended_movie_names[6])
    with col8:
        st.image(recommended_movie_posters[7], use_column_width='always')
        st.text(recommended_movie_names[7])
    with col9:
        st.image(recommended_movie_posters[8], use_column_width='always')
        st.text(recommended_movie_names[8])





