import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('electiondata4.csv')

data['votes'] = pd.to_numeric(data['votes'], errors='coerce')

st.title('Election 2024 India Analysis')

states = data['state'].unique()
selected_state = st.selectbox('Select a state', states)

constituencies = data[data['state'] == selected_state]['constituency'].unique()
selected_constituency = st.selectbox('Select a constituency', constituencies)

candidates = data[data['constituency'] == selected_constituency]['Name'].unique()
selected_candidate = st.selectbox('Select Candidate', candidates)

def plot_constituency(state, constituency):
    df = data[(data['state'] == state) & (data['constituency'] == constituency)]
    
    df['votes'] = pd.to_numeric(df['votes'], errors='coerce')
    
    plt.figure(figsize=(12, 8))
    barplot = sns.barplot(x='Name', y='votes', data=df, hue='won status', palette='viridis')
    
    plt.title(f'Election Results in {constituency}, {state}', fontsize=16)
    plt.xlabel('Candidate', fontsize=12)
    plt.ylabel('Votes', fontsize=12)
    plt.xticks(rotation=45, ha='right')
    
    for p in barplot.patches:
        barplot.annotate(format(p.get_height(), '.0f'), 
                         (p.get_x() + p.get_width() / 2., p.get_height()), 
                         ha='center', va='center', 
                         xytext=(0, 9), 
                         textcoords='offset points')
    
    plt.legend(title='Won Status')
    st.pyplot(plt)

def plot_candidate(constituency, candidate):
    df = data[(data['constituency'] == constituency) & (data['Name'] == candidate)]
    df['votes'] = pd.to_numeric(df['votes'], errors='coerce')
    
    plt.figure(figsize=(12, 8))
    barplot = sns.barplot(x='Name', y='votes', data=df, hue='won status', palette='viridis')
    
    plt.title(f'Election Results for {candidate} in {constituency}', fontsize=16)
    plt.xlabel('Candidate', fontsize=12)
    plt.ylabel('Votes', fontsize=12)
    plt.xticks(rotation=45, ha='right')
    
    for p in barplot.patches:
        barplot.annotate(format(p.get_height(), '.0f'), 
                         (p.get_x() + p.get_width() / 2., p.get_height()), 
                         ha='center', va='center', 
                         xytext=(0, 9), 
                         textcoords='offset points')
    
    plt.legend(title='Won Status')
    st.pyplot(plt)

if st.button('Show Results'):
    plot_constituency(selected_state, selected_constituency)
    plot_candidate(selected_constituency, selected_candidate)
