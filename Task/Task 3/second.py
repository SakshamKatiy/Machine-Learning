import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from streamlit_option_menu import option_menu

def selected():
   div = f"""
   <div style="width:100%;display:flex;gap:18vw">
   <div style="height:60vh;width:25vw;border-radius:10px;background-color:#0898a0">
      <div>
         <h3 style='text-align:center;background-color:white;position:relative;bottom:20px;width:20vw;margin-left:30px;box-shadow: 3px 3px #888888;border-radius:10px;'>Andhra Pradesh</h3>
      </div>
      <p style="color:white;margin-left:30px;">Assembly Constituencies</p>
      <p style="color:white;margin-left:30px;">*Status of Top Five Parties</p>
      <div style="background-color:white;height:40vh;width:20vw;margin-left:30px;margin-top:20px;border-radius:8px;box-shadow: 3px 3px #888888;">
         <div><p>Parties<span style="text-align:end"> Leading/Won</span></p></div>
         <div style="background-color:#f0f0f0;margin-top:4px">
            <h5>TDP<span style="margin-left:200px">135 </span></h5>
         </div>
         <div style="background-color:#f0f0f0;margin-top:4px">
            <h5>JnP<span style="margin-left:210px">21</span></h5>
         </div>
         <div style="background-color:#f0f0f0;margin-top:4px">
            <h5>YSRCP<span style="margin-left:186px">11</span></h5>
         </div>
         <div style="background-color:#f0f0f0;margin-top:4px">
            <h5>BJP<span style="margin-left:215px">8</span></h5>
         </div>
         <div style="width:12vw;height:8vh;text-align:center;border:1px solid blue;margin-left:60px;margin-top:10px;border-radius:10px;padding-top:8px;position:fixed;z-index:111;">Details</div>
      </div>
   </div>

   <div style="height:60vh;width:25vw;border-radius:10px;background-color:#800000">
      <div>
         <h3 style='text-align:center;background-color:white;position:relative;bottom:20px;width:20vw;margin-left:30px;box-shadow: 3px 3px #888888;border-radius:10px'>Odisha</h3>
      </div>
      <p style="color:white;margin-left:30px;">Assembly Constituencies</p>
      <p style="color:white;margin-left:30px;">*Status of Top Five Parties</p>
      <div style="background-color:white;height:40vh;width:20vw;margin-left:30px;margin-top:20px;border-radius:8px;box-shadow: 3px 3px #888888;">
         <div><p>Parties<span style="text-align:end"> Leading/Won</span></p></div>
         <div style="background-color:#f0f0f0;margin-top:4px">
            <h5>BJP<span style="margin-left:200px">78 </span></h5>
         </div>
         <div style="background-color:#f0f0f0;margin-top:4px">
            <h5>BJD<span style="margin-left:210px">51</span></h5>
         </div>
         <div style="background-color:#f0f0f0;margin-top:4px">
            <h5>INC<span style="margin-left:186px">14</span></h5>
         </div>
         <div style="background-color:#f0f0f0;margin-top:4px">
            <h5>IND<span style="margin-left:215px">3</span></h5>
         </div>
         <div style="background-color:#f0f0f0;margin-top:4px">
            <h5>CPI(M)<span style="margin-left:215px">1</span></h5>
         </div>
      </div>
   </div>
</div>

   """
   st.markdown(div,unsafe_allow_html=True)

    


