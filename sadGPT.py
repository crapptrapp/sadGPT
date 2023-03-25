import streamlit as st
st.set_page_config(page_title="sadGPT quotes based on https://huggingface.co/datasets/Crapp/sadQuotes")#,page_icon=img)
hide_menu_style = """
        <style>
        MainMenu {visibility: hidden; }
        footer {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)
import pandas as pd
quotes=pd.read_csv("https://huggingface.co/datasets/Crapp/sadQuotes/raw/main/quotes.csv",header=None)
quotes=quotes.fillna('')
import random
rowZ=len(quotes)
rowN=65#check for one of the empty quotes
rowN=random.randint(0,rowZ-1)
quoteS=''.join(quotes.loc[[rowN]][1])
quoteS=quoteS.strip()
quoteS=" ".join(quoteS.split())
quoteL=''.join(quotes.loc[[rowN]][0])#.to_string()
collectI="What is purpose of Life?"
st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
st.write("Trying #sadGPT on ",quoteL)
if quoteS: st.write("\"",quoteS,"\"")
else:  st.write("emptiness...")
collectO=st.text_input("Lets try #sadGPT on our own, like",collectI)
if collectO==collectI: st.write("Purpose of Life is to have no Purpose.")
else: st.write(collectO)
