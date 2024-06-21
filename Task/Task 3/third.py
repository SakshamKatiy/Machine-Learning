import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
st.set_page_config(layout="wide")
def selected():
    
    data = pd.read_csv('India_Election_Results_2024.csv')
    st.write(data)
    
    for index, row in data.iterrows():
        
        div = f"""
        <div style="display:flex"; gap:4vw>
        <div style="background-color: #f0f0f0; 
        border:2px solid red;width:20vw;height:40vh;padding: 1rem;  border-radius: 5px; text-align:center">
            <h5>{row['State']}</h5>
            <h5>{row['Assembly Constituency']}</h5>
            <h3>{'Won'}</h3>
            <p>{row['Winner']}</p>
            <p>{row['Winner Party']}</p>
        </div>
        </div>
        </div>
        """
        st.markdown(div, unsafe_allow_html=True)