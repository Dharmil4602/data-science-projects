import streamlit as st
import pandas as pd
import seaborn as sns

# Adding Title
st.title("Data Analysis")
st.subheader("Data analysis using python and streamlit")

# Giving user the option to upload dataset
file_upload = st.file_uploader("Upload your dataset")
if file_upload is not None:
    data = pd.read_csv(file_upload)

# Showing the dataset
