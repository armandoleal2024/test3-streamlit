import streamlit as st

st.title("Open AI ")
st.sidebar.title("AI Apps")

# Set the page config to wide mode
st.set_page_config(layout="wide")

applications = ["Blog Generation", "Generate Image", "Movie Recommendation"]
application_choice = st.sidebar.radio("Choose an Application", applications)
