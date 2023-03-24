import pandas as pd
import streamlit as st

st.set_page_config(page_title="Test Decision Tree", page_icon="🌲", layout="centered")

st.title("🖥 Please enter variables")
st.subtitle("Use decimals")
    
with st.form("my_form"):
    left, right = st.columns((1, 10))
    
    M = right.number_input("Margin")
    left, right = st.columns(2)
    G = left.number_input("Growth")
    R = right.number_input("Retention")
    
    N = left.number_input("Avg MRR")

    submit = st.form_submit_button()
    
    
if M < 0.3 and G < 0.15 and R < 0.9:
    A = 1.6
elif M < 0.3 and G < 0.15 and R < 0.95:
    A = 1.7
elif M < 0.3 and G < 0.15 and R >= 0.95:
    A = 1.8

elif M < 0.3 and G < 0.5 and R < 0.9:
    A = 1.9
elif M < 0.3 and G < 0.5 and R < 0.95:
    A = 2.0
elif M < 0.3 and G < 0.5 and R >= 0.95:
    A = 2.1

elif M < 0.3 and G >= 0.5 and R < 0.9:
    A = 2.2
elif M < 0.3 and G >= 0.5 and R < 0.95:
    A = 2.3
elif M < 0.3 and G >= 0.5 and R >= 0.95:
    A = 2.4

elif M < 0.6 and G < 0.15 and R < 0.9:
    A = 2.0
elif M < 0.6 and G < 0.15 and R < 0.95:
    A = 2.21
elif M < 0.6 and G < 0.15 and R >= 0.95:
    A = 2.42

elif M < 0.6 and G < 0.5 and R < 0.9:
    A = 2.63
elif M < 0.6 and G < 0.5 and R < 0.95:
    A = 2.84
elif M < 0.6 and G < 0.5 and R >= 0.95:
    A = 3.05
    
elif M < 0.6 and G >= 0.5 and R < 0.9:
    A = 3.26
elif M < 0.6 and G >= 0.5 and R < 0.95:
    A = 3.47
elif M < 0.6 and G >= 0.5 and R >= 0.95:
    A = 3.68

elif M >= 0.6 and G < 0.15 and R < 0.9:
    A = 2.84
elif M >= 0.6 and G < 0.15 and R < 0.95:
    A = 3.05
elif M >= 0.6 and G < 0.15 and R >= 0.95:
    A = 3.25

elif M >= 0.6 and G < 0.5 and R < 0.9:
    A = 3.45
elif M >= 0.6 and G < 0.5 and R < 0.95:
    A = 3.75
elif M >= 0.6 and G < 0.5 and R >= 0.95:
    A = 4.1

elif M >= 0.6 and G >= 0.5 and R < 0.9:
    A = 3.05
elif M >= 0.6 and G >= 0.5 and R < 0.95:
    A = 4.55
elif M >= 0.6 and G >= 0.5 and R >= 0.95:
    A = 4.85


if submit:
    Valuation = A * N * 12
    st.balloons()
    st.success(Valuation)
