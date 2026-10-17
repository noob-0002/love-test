import streamlit as st
import pandas as pd
from datetime import datetime
from streamlit_gsheets import GSheetsConnection

st.set_page_config(page_title="Let's Rate Your Love", page_icon="❤️")
st.title("Let's Rate Your Love ❤️")

conn = st.connection("gsheets", type=GSheetsConnection)

with st.form("love_test"):
    name = st.text_input("Name of your love")
    age = st.number_input("Age", min_value=1, max_value=120, step=1)
    submitted = st.form_submit_button("Test")

if submitted:
    if name:
        try:
            new_row = pd.DataFrame([{
                "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "Name": name,
                "Age": age
            }])
            existing_data = conn.read(worksheet="Sheet1", usecols=[0, 1, 2], ttl=0)
            updated_data = pd.concat([existing_data, new_row], ignore_index=True)
            conn.update(worksheet="Sheet1", data=updated_data)
        except Exception as e:
            print(f"Logging failed: {e}")

    st.success("No need for test, your love is deep enough and you complete me.")
    st.balloons()
