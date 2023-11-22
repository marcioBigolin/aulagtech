import streamlit as st
import pandas as pd

st.write("meu teste alterado")
dado = pd.read_csv("data.csv")

st.write(dado)