
import streamlit as st

def addition(x,y):
 return(x+y)


st.title("Calculator")

x = st.number_input()
y = st.number_input()

st.write(addition(x,y))
