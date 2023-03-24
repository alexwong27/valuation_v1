import pandas as pd
import streamlit as st

st.set_page_config(page_title="Test Decision Tree", page_icon="🌲", layout="centered")

st.title("🖥 Valuation tool")

with st.form("my_form"):
    left, right = st.columns((1, 10))
    color = left.color_picker("Color", value="#b4cffa")
    M = right.number_input("Margin", value=0.30)
    left, right = st.columns(2)
    G = left.number_input("Growth", value=0.15)
    R = right.number_input("Retention", value=0.95)
    product_type = left.selectbox("Product type", ["Data app crafting", "ML model training"])
    N = right.number_input("Avg MRR", value=25000)
    price_per_unit = st.slider("Price per unit", 1, 100, 60)
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
