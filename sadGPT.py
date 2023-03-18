import streamlit as st
#st.write('Hello world!')
st.set_page_config(page_title="sadGPT quotes based on https://huggingface.co/datasets/Crapp/sadQuotes")#,page_icon=img)
hide_menu_style = """
        <style>
        MainMenu {visibility: hidden; }
        footer {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)
from annotated_text import annotated_text
annotated_text(("sadGPT","#faa"))
st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
quote=st.text_input("What is purpose of Life?", "Purpose of Life is to have no Purpose.")
st.write("Trying transformer on...")
st.write(quote)
