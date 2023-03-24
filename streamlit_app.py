import pandas as pd
import streamlit as st

st.set_page_config(page_title="Test Decision Tree", page_icon="🌲", layout="centered")

st.title("🖥 Valuation tool")

form = st.form(key="annotation")

with st.form("template_form"):
    left, right = st.columns((1, 10))
    M = right.input("Margin", value=0.3)
    left, right = st.columns(2)
    G = left.input("Growth", value=0.15)
    R = right.input("Retention", value=0.95)
    N = left.input("Average MRR", value=25000)
    
    Valuation = A * N * 12
    submit = st.form_submit_button()

if submitted:
   
    st.success(Valuation)
    st.balloons()
