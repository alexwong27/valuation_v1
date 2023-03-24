import pandas as pd
import streamlit as st

st.set_page_config(page_title="Test Decision Tree", page_icon="🌲", layout="centered")

st.title("🖥 Valuation tool")

with st.form("my_form"):
    cols = st.columns((1, 2))
    M = cols[0].number_input("Margin:")
    G = cols[1].number_input("Growth:")
    R = cols[2].number_input("Retention:")
    N = cols[1].number_input("Avg MRR:")
    st.form_submit_button(label="Submit")
    submitted = st.form_submit_button(label="Submit")
    
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

#node2 margin < 60%
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

#node3 margin >= 60%
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

    Valuation = A * N * 12
    submit = st.form_submit_button()

if submitted:
   
    st.success(Valuation)
    st.balloons()
