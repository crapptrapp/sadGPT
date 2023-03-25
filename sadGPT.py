import streamlit as st
st.set_page_config(page_title="sadGPT quotes based on https://huggingface.co/datasets/Crapp/sadQuotes")#,page_icon=img)
#st.title("sadGPT quotes based on https://huggingface.co/datasets/Crapp/sadQuotes")
hide_menu_style = """
        <style>
        MainMenu {visibility: hidden; }
        footer {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)
import pandas as pd
#https://docs.streamlit.io/library/get-started/create-an-app
#@st.cache_data
def load_data(URL):
  quotes=pd.read_csv(URL,header=None)
  quotes=quotes.fillna('')
  return quotes
quotes=load_data("https://huggingface.co/datasets/Crapp/sadQuotes/raw/main/quotes.csv")
import random
rowZ=len(quotes)
rowN=65#check for one of the empty quotes
rowN=356#longest
rowN=1578#shortest
import datetime
current_time = datetime.datetime.now()
st.text(current_time)
seed=current_time.day
random.seed(seed)
rowN=random.randint(0,rowZ-1)
quoteS=''.join(quotes.loc[[rowN]][1])
quoteS=quoteS.strip()
quoteS=" ".join(quoteS.split())
quoteL=''.join(quotes.loc[[rowN]][0])#.to_string()
#set_seed(42)
#from transformers import pipeline, set_seed
#generator = pipeline('text-generation', model='gpt2')
collectI="What is the purpose of Life?"
st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
st.write("Trying #sadGPT on ",quoteL)
if quoteS: st.write("\"",quoteS,"\"")
else:  st.write("emptiness...")
collectO=st.text_input("Lets try #sadGPT on our own, like",collectI)
if collectO==collectI: st.write("Purpose of Life is to have no Purpose.")
else: st.write(collectO)
