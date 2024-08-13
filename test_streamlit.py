import streamlit as st

st.title("Open AI ")
st.sidebar.title("AI Apps")

applications = ["Blog Generation", "Generate Image", "Movie Recommendation","Other"]
application_choice = st.sidebar.radio("Choose an Application", applications)
