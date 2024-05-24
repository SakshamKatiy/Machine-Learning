import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
# import pillow as pil

st.title('Machine Learning Data clining')
st.error('Cleaning Successfully')

df=pd.read_csv('20.csv')
# st.dataframe(df)
fig = plt.figure()
plt.plot(df)
st.pyplot(fig)
