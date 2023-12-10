import streamlit as st
import os

from dotenv import  load_dotenv
from utils.data_processing import  *
from utils.vector_embeddings_v2 import  *

load_dotenv()

TARGET_DIR="./uploaded_data"
VECTOR_DB_DIR="./docs/chroma"
st.header("Upload Resumes",divider='rainbow')
uploaded_files = st.file_uploader("Upload your files",type=['pdf','docx'],accept_multiple_files=True)


if len(uploaded_files) > 0 :
    val = store_uploaded_files(uploaded_files,target_dir=TARGET_DIR)
    is_df_created = get_feature_df(target_dir=TARGET_DIR)
    if is_df_created :
        vector_store = get_vector_store(VECTOR_DB_DIR)


