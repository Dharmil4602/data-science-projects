import streamlit as st
import pandas as pd
st.title("Motor Vehicle Collisions in New York City")
st.markdown("This application is a Streamlit dashboard that can be used to analyze motor vehicle collisions in NYC 🗽💥🚗")

@st.cache(persist=True)
def load_data(nrows):
    data = pd.read_csv('data.csv', nrows=nrows, parse_dates=[['CRASH_DATE', 'CRASH_TIME']])
    data.dropna(subset=['LATITUDE', 'LONGITUDE'], inplace=True)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data.rename(columns={'crash_date_crash_time': 'date/time'}, inplace=True)
    return data

data = load_data(100000)

# Showing the data with different options to filter
st.header("Where are the most injured people in NYC?")
injured_people = st.slider("Number of persons injured in vehicle collisions", 0, 19)
st.map(data.query('injured_persons >= @injured_people')[['latitude', 'longitude']].dropna(how="any"))

# Here on changing the hour, the data will be updated 
st.header("How many collisions occur during a given time of day?")
hour = st.slider("Hour to look at", 0, 23)
data = data[data['date/time'].dt.hour == hour]






if st.checkbox("Show Raw Data", False):
    st.subheader("Raw data")
    st.write(data)
    