import streamlit as st
import pandas as pd
DATA_URL = pd.read_csv('data.csv')
st.title("Motor Vehicle Collisions in New York City")
st.markdown("This application is a Streamlit dashboard that can be used to analyze motor vehicle collisions in NYC 🗽💥🚗")