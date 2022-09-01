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
# First check that user has uploaded the dataset
if file_upload is not None: # Check that user has uploaded the dataset
    if st.checkbox("Preview Dataset"):
        if st.button("Head"):
            st.write(data.head())
        if st.button("Tail"):
            st.write(data.tail())

# Showing Data Types
if file_upload is not None:
    if st.checkbox("Show Data Types"):
        st.write(data.astype(str))

# Finding shape of the data set
if file_upload is not None:
    if st.checkbox("Show Shape"):
        st.write("Number Of Rows:",data.shape[0])
        st.write("Number Of Columns:",data.shape[1])

# Display null values
if file_upload is not None:
    test_null = data.isnull().values.any()
    if test_null == True:
        if st.checkbox("Show Null Values"):
            sns.heatmap(data.isnull())
            st.pyplot()
    else:
        st.success("No Null Values")