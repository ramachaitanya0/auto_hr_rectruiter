import streamlit as st
import os
def create_folder(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
@st.cache_data
def store_uploaded_files(uploaded_files:list,target_dir:str):
    create_folder(target_dir)
    print("Created the directory for the uploaded files")
    for uploaded_file in uploaded_files:
        file_path = os.path.join(target_dir, uploaded_file.name)
        with open(file_path, "wb") as f:
            f.write(uploaded_file.read())
    print("Written all the files successfully")
    return True