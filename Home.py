import pandas as pd
import streamlit as st
import os , shutil
import numpy as np
from dotenv import  load_dotenv
from utils.data_processing import  *
from utils.vector_embeddings_v2 import  *
from utils.hr_message import *
st.set_page_config(page_icon="👋",page_title="Home")
load_dotenv()
TARGET_DIR="./uploaded_data"
VECTOR_DB_DIR="./docs/chroma"

st.header("Welcome to IntelliHire" , divider='rainbow')

def delete_folder(folder_path):
    try:
        if os.path.isdir(folder_path) :
            # os.rmdir(folder_path)
            shutil.rmtree(folder_path)
    except Exception as e:
        st.error(f"Error deleting folder {folder_path}: {e}")

if "Amount_Spent" not in st.session_state :
    st.session_state["Amount_Spent"] = 0.0

amount_spent_submit = st.sidebar.button("Get Amount Spent")
if amount_spent_submit :
    amount_spent_in_rupees = np.float64(st.session_state.Amount_Spent) * 80
    amount_spent = st.sidebar.empty()
    amount_spent.text(f"""
    Amount spent in Dollars is ${st.session_state.Amount_Spent} 
    Amount spent in Rupees is Rs.{amount_spent_in_rupees}
""")

if "clean_previous_session_data" not in st.session_state :
    st.session_state["clean_previous_session_data"] = 1
    delete_folder("./docs/")
    delete_folder("./uploaded_data/")


if "created_all_applicants_df" not in st.session_state :
    st.session_state['created_all_applicants_df']=1
    df = pd.read_excel("data/all_applicants.xlsx")
    df = df.iloc[0:0]
    df.to_excel("./data/all_applicants.xlsx")

    df1 = pd.read_excel("data/technical_filtered.xlsx")
    df1 = df1.iloc[0:0]
    df1.to_excel("./data/technical_filtered.xlsx")

    df2 = pd.read_excel("data/matching_profiles.xlsx")
    df2 = df2.iloc[0:0]
    df2.to_excel("./data/matching_profiles.xlsx")



st.markdown(
    """
    Welcome to the IntelliHire! This powerful tool is designed to streamline
    and enhance your recruiting process. Whether you're a seasoned HR professional or just
    getting started, our app offers a range of features to make your job easier and more efficient.

    ### Key Features:

    ##### 1. Document Upload Capability
    Upload and manage candidate documents seamlessly, making it easy to keep track of important
    files and information.

    ##### 2. Interactive and User-Friendly Chat Interface
    Communicate with candidates effortlessly through our interactive chat interface. Enhance
    the candidate experience and streamline communication.

    ##### 3. Automated Recommendations
    Leverage intelligent algorithms to receive automated recommendations for potential candidates
    based on your specific criteria.


    ##### 4. Job Description Generator
    Create tailored job descriptions effortlessly by inputting your company's requirements. Save time
    and ensure clarity in your job postings.

    ##### 5. Question and Answer Generator
    Generate relevant interview questions and answers based on the required role, experience level,
    and other parameters. Enhance your interview process with targeted and insightful questions.
    
    ##### 6. Session Spending Tracker
    Keep an eye on resource allocation with the ability to check the amount spent in each recruiting
    session. Stay within budget and optimize your recruiting efforts.

    Get ready to revolutionize your recruiting process with the HR Recruiting Assistant App!
    """
)










