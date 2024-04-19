import streamlit as np

def add(a,b):
  return a+b

a = st.number_input("first number :", )
b = st.number_input("second number :", )

st.text(add(a,b))
