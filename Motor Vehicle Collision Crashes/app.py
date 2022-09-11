import streamlit as st
import pandas as pd
st.title("Motor Vehicle Collisions in New York City")
st.markdown("This application is a Streamlit dashboard that can be used to analyze motor vehicle collisions in NYC 🗽💥🚗")

@st.cache(persist=True)
def load_data(nrows):
    data = pd.read_csv('data.csv', nrows=nrows, parse_dates=[['CRASH DATE', 'CRASH TIME']])
    data.dropna(subset=['LATITUDE', 'LONGITUDE'], inplace=True)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data.rename(columns={'crash date_crash time': 'date/time'}, inplace=True)
    return data

data = load_data(100000)
if st.checkbox("Show Raw Data", False):
    st.subheader("Raw data")
    st.write(data)
    