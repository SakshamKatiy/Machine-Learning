import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from streamlit_option_menu import option_menu
import first,second,third
# Header
div =f"""
<div style="background-color:#a70529"><img src="https://results.eci.gov.in/PcResultGenJune2024/img/eci-logo.png">
<img style="height:60px ;margin-left:320px" src="https://results.eci.gov.in/PcResultGenJune2024/img/deshgarv-logo.png">
</div>
"""
st.markdown(div,unsafe_allow_html=True)
st.warning("Disclaimer : ECI is displaying the information as being filled in the system by the Returning Officers from their respective Counting Centres.The final data for each AC/PC will be shared in Form-20.")
st.title('Election 2024 India Analysis')

# with st.sidebar:
def run():
    selected = option_menu(
            menu_title="Main Menu",
            options = ["Parliamentary Constituency", "Assembly Constituency General", "Assembly Constituency Bye"],
            orientation="horizontal",
            styles={
                "nav-link":{"--hover-color":"red","font-size":"16px"},
                "nav-link-selected":{"font-size":"16px"}
            }
        )
    if selected == "Parliamentary Constituency":
        st.title(f" {selected}") 
        first.selected()  
    if selected == "Assembly Constituency General":
        st.title(f" {selected}")  
        second.selected()   
    if selected == "Assembly Constituency Bye":
        st.title(f"{selected}") 
        third.selected()    
run()
class MultiPage:
    def __init__(self) -> None:
        pass 
    
    
data = pd.read_csv('electiondata4.csv')

data['votes'] = pd.to_numeric(data['votes'], errors='coerce')


st.sidebar.success('General Election to Parliamentary Constituencies: Trends & Results June-2024')
states = data['state'].unique()
selected_state = st.sidebar.selectbox('Select a state', states)

constituencies = data[data['state'] == selected_state]['constituency'].unique()
selected_constituency = st.sidebar.selectbox('Select a constituency', constituencies)

candidates = data[data['constituency'] == selected_constituency]['Name'].unique()
selected_candidate = st.sidebar.selectbox('Select Candidate', candidates)

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

    if st.sidebar.button('Show Results'):
        plot_constituency(selected_state, selected_constituency)
        plot_candidate(selected_constituency, selected_candidate)
    
