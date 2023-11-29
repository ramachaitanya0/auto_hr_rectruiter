import streamlit as st
import os

from dotenv import  load_dotenv
from utils.data_processing import  *
from utils.vector_embeddings import  *
from utils.hr_message import *

load_dotenv()
TARGET_DIR="./uploaded_data"
st.title("Auto HR Recruiter")
st.header("Upload Files",divider='rainbow')
uploaded_files = st.file_uploader("Upload your files",type=['pdf','docx'],accept_multiple_files=True)


if len(uploaded_files) > 0 :
    val = store_uploaded_files(uploaded_files,target_dir=TARGET_DIR)
    feature_df = get_feature_df(target_dir=TARGET_DIR)
    vector_store = get_vector_store(feature_df)
    print("Created Embeddings Successfully ")


st.header("Profile Matcher",divider='blue')
job_description = st.text_input("Enter Job Description Here")
submit = st.button('Get Matching Profiles')
if submit :
    df = get_matching_profiles(job_description,vector_store)
    st.dataframe(df,width=1000)

st.header("Send Automated Mails to Potential Candidates",divider='rainbow')
cols = st.columns(3)
with cols[0] :
    job_position = st.text_input("Job Position")
with cols[1] :
    HR_Name = st.text_input("HR Name")
with cols[2] :
    test_link = st.text_input("Test URL")


send = st.button("Send Mails to Potential Candidates")
if send :
    for i in range(df.shape[0]):
        email = df.loc[i,"mail_id"]
        candidate_name = df.loc[i,"Name"]
        val = send_mail(reciever_mail=email,job_position=job_position,candidate_name=candidate_name,HR_Name=HR_Name,test_link=test_link)

    st.write("Successfully sent mail to all the Potential Candidates ")












