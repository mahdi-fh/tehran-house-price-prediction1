
import streamlit as st
import numpy as np
import pandas as pd
import joblib

model = joblib.load('knrpipe.joblib')
st.title('مشخصات خانه موردنظر خود را وارد کنید ')

Room = st.slider("How many room?",['0,2'])
Parking = ('yes','No')
st.radio("Have Parking?",Parking)
Elevator = ('yes','No')
st.radio("Have Elevator?",Elevator)
Address = st.selectbox("Wher is Home?",['Pardis','Parand','Dorous','Shahrake Qods','Punak'])
