import streamlit as st
st.set_page_config(page_title = "Student Information", layout = "centered")
st.title('Student Profile Application')
st.caption("Launched by DEEKSHITHA DS")
st.caption('Fill in your details and click View My profile.')
name = st.text_input("Student Name")
roll_no = st.text_input("USN / Roll Number")
dept = st.text_input['Department',["CSE", "ISE", "ECE", "EEE", "ME", "Civil"])
