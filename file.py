
import streamlit as st

def addition(x,y):
 return(x+y)


st.title("Calculator")

x = st.number_input("first number :" )
y = st.number_input("second number :" )

st.text("The addition of x and y is :")
st.write(addition(x,y))
