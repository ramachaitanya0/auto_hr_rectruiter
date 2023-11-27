import streamlit as st
import os
import pandas as pd
import openai

from langchain.output_parsers import StructuredOutputParser
from langchain.chat_models import ChatOpenAI


from dotenv import  load_dotenv
from utils.data_processing import  *
from utils.vector_embeddings import  *

load_dotenv()
TARGET_DIR="./uploaded_data"
st.title("Auto HR Recruiter")
uploaded_files = st.file_uploader("Upload your files",type=['pdf'],accept_multiple_files=True)


if len(uploaded_files) > 0 :
    val = store_uploaded_files(uploaded_files,target_dir=TARGET_DIR)
    feature_df = get_feature_df(target_dir=TARGET_DIR)
    vector_store = get_vector_store(feature_df)
    print("Created Embeddings Successfully ")


job_description = st.text_input("Enter Job Description Here")
submit = st.button('Get Matching Profiles')
if submit :
    df = get_matching_profiles(job_description,vector_store)
    st.dataframe(df)














