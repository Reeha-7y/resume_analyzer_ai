import os
from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import google.generativeai as genai

from pdf import extract_text # method in pdf.py file

key = os.getenv('GOOGLE_API_KEY')

genai.configure(api_key=key)

model = genai.GenerativeModel('gemini-2.5-flash-lite')

def analyze_resume(pdf_doc , job_des):
    
    if pdf_doc is not None:
        pdf_text = extract_text(pdf_doc)
        st.write(f'Text extracted successfully ✅')
        
    else:
        st.warning('Error !! Drop the file in PDF format ⟳')
    ats_score = model.generate_content(f'''Compare the given pdf {pdf_text}
                                       and given job description {job_des}
                                       and provide ATS score
                                       on scale of 0 to 100.
                                       
                                       Generate the results in bullet points
                                       (maximum 5 points)''')
    
    probability = model.generate_content(f'''Compare the given pdf {pdf_text}
                                         and given job description {job_des}
                                         and provide the probability to get
                                         short listed for the given job description
                                         on scale of 0 to 100.
                                         
                                         Generate the results in bullet points
                                         (maximum 5 points)''')
    
    good_fit = model.generate_content(f'''Compare the given pdf {pdf_text}
                                         and given job description {job_des}
                                         and say whether my resume is good fit to the given
                                         job description.If yes provide the details and if no, 
                                         provide explaination
                                         
                                         
                                         Generate the results in bullet points
                                         (maximum 5 points)''')
    
    skill_match = model.generate_content(f'''Compare the given pdf {pdf_text}
                                         and given job description {job_des}
                                         and give matched skill for the given job description
                                         and also give missing skills
                                         
                                         Generate the results in bullet points
                                         (maximum 5 points)''')
    
    missing_values = model.generate_content(f'''Compare the given pdf {pdf_text}
                                         and given job description {job_des}
                                         and give the missing details in resume and also additional details
                                         that can be added to resume
                                         
                                         Generate the results in bullet points
                                         (maximum 5 points)''')
    
    
    
    swot = model.generate_content(f'''Compare the given pdf {pdf_text}
                                      and given job description {job_des}
                                      and perform SWOT analysis
                                         
                                      Generate the results in bullet points
                                      (maximum 5 points)''')
    
    return{st.write(ats_score.text),
           st.write(probability.text),
           st.write(good_fit.text),
           st.write(skill_match.text),
           st.write(missing_values.text),
           st.write(swot.text)}
    
      