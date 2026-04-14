import streamlit as st
from analysis import analyze_resume # method in analysis.py

st.set_page_config(page_title='Resume Analyzer', page_icon='📄')
st.title('Resume Analyzer using AI 💻 ֎🇦🇮')
st.header(' :blue[AI powered Resume analyser with given job desciption using AI 🤖ིྀ]')
st.subheader(''' This page helps you to compare the resume and the givne job description and provide the ATS score, probability score, goodness of fit score, skills match score, missing keywords and SWOT analysis of the resume for the given job description.''')
st.sidebar.subheader('Drop your resume here 📑')
pdf_doc = st.sidebar.file_uploader('Click here' , type = ['pdf'])

st.sidebar.markdown('Designed by Reeha Rafi 📩')
st.sidebar.markdown('Git Hub : https://github.com/Reeha-7y/resume_analyzer_ai')

job_des = st.text_area('Copy and paste the JD here ✍️' , max_chars = 10000)

submit = st.button('Get Results 🎯')

if submit:
    with st.spinner('Loading.....⏳'):
        analyze_resume(pdf_doc , job_des)

