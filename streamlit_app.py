import pandas as pd
import streamlit as st

st.set_page_config(page_title="Test Decision Tree", page_icon="🌲", layout="centered")

st.title("🖥 Valuation tool")

form = st.form(key="annotation")

with form:
    cols = st.columns((1, 1))
    M = cols[0].input("Margin:")
    bug_type = cols[1].selectbox(
        "Bug type:", ["Front-end", "Back-end", "Data related", "404"], index=2
    )
    comment = st.text_area("Comment:")
    cols = st.columns(2)
    date = cols[0].date_input("Bug date occurrence:")
    bug_severity = cols[1].slider("Bug severity:", 1, 5, 2)
    submitted = st.form_submit_button(label="Submit")


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
