import pandas as pd
import streamlit as st
import os , shutil
import numpy as np
from dotenv import  load_dotenv
from utils.data_processing import  *
from utils.vector_embeddings_v2 import  *
from utils.hr_message import *

load_dotenv()
TARGET_DIR="./uploaded_data"
VECTOR_DB_DIR="./docs/chroma"
st.title("IntelliHire")

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
    df = pd.read_csv("data/all_applicants.csv")
    df = df.iloc[0:0]
    df.to_csv("./data/all_applicants.csv")

    df1 = pd.read_csv("./data/technical_filtered.csv")
    df1 = df1.iloc[0:0]
    df1.to_csv("./data/technical_filtered.csv")

    df2 = pd.read_csv("./data/matching_profiles.csv")
    df2 = df2.iloc[0:0]
    df2.to_csv("./data/matching_profiles.csv")

# # Title
# st.title("HR Recruiting Assistant")

# Description
st.markdown(
    """
    Welcome to the HR Recruiting Assistant! This application is designed to streamline and enhance the recruiting process at **TVS**, making it easier for HR professionals to manage applicants effectively.

    ## Features

    - **Profile Matching:** Easily fetch matching profiles based on job descriptions, ensuring a more efficient screening process.

    - **Automated Emails:** Send automated emails to applicants based on their current stage in the recruitment process, keeping them informed and engaged.

    - **Task Management:** Stay organized with built-in task management features to track the progress of each applicant through the hiring stages.

    - **Data Visualization:** Gain insights into the recruitment pipeline with interactive charts and graphs, helping you make informed decisions.

    ## How to Use

    1. **Profile Matching:**
       - Enter the job description details.
       - Click on the "Fetch Matching Profiles" button to get a list of relevant candidates.

    2. **Automated Emails:**
       - Manage applicant stages using the sidebar.
       - The system will automatically send emails based on predefined templates.

    3. **Task Management:**
       - Track tasks and milestones for each applicant.
       - Update task status as you progress through the recruitment process.

    4. **Data Visualization:**
       - Explore visual representations of recruitment data to identify trends and areas for improvement.

    ## Get Started
    Ready to revolutionize your recruitment process? Start by exploring the features on the sidebar. If you have any questions, check out the documentation or reach out to our support team.

    Happy recruiting!
    """
)










