import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from streamlit_option_menu import option_menu

# Header
def selected():
    # First.csv
    df = pd.read_csv('first.csv')
    df

    df = pd.DataFrame({
        'Party': df['Party'],
        'Won': df['Won']
    })
    df['Won'] = pd.to_numeric(df['Won'])
    total_votes = df['Won'].sum()
    df['Percentage'] = (df['Won'] / total_votes) * 100

    fig, ax = plt.subplots(figsize=(6, 8))
    wedges, texts, autotexts = ax.pie(
        df['Won'], 
    #     labels=data['Party'], 
        autopct='', 
        startangle=140,
    )


    legend_labels = [f"{party}: {percentage:.1f}%" for party, percentage in zip(df['Party'], df['Percentage'])]

    plt.axis('equal')
    plt.legend(wedges, legend_labels, title="Parties", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

    st.pyplot(fig)
    
    
    st.write(df)