import streamlit as st

st.set_page_config(page_title="Let's Rate Your Love", page_icon="❤️")

st.title("Let's Rate Your Love ❤️")

with st.form("love_test"):
    name = st.text_input("Name of your love")
    age = st.number_input("Age", min_value=1, max_value=120, step=1)
    submitted = st.form_submit_button("Test")

if submitted:
    st.success(
        "No need for test, your love is deep enough and you complete me."
    )
    st.balloons()
