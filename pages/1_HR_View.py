import pandas as pd

from utils.vector_embeddings_v2 import  *
from utils.hr_message import *

VECTOR_DB_DIR="./docs/chroma"

st.header("Profile Matcher",divider='blue')
job_description = st.text_input("Enter Job Description Here")
submit = st.button('Get Matching Profiles')

if "get_matching_profiles_button" not in st.session_state :
    st.session_state['get_matching_profiles_button'] = 0

if submit :
    st.session_state['get_matching_profiles_button'] = 1

if st.session_state['get_matching_profiles_button']:
    df = get_matching_profiles(job_description, VECTOR_DB_DIR)
    df.to_excel("./data/matching_profiles.xlsx")
    st.dataframe(df[["Applicant_Name","years_of_exp","Key_Skills","Linkedin_Profile","GitHub_Profile","Mail_Id"]], width=1000)


st.header("Filtered Profiles",divider='blue')
submit = st.button('Get filtered Profiles')
if "get_filtered_profiles_button" not in st.session_state :
    st.session_state['get_filtered_profiles_button'] = 0

if submit :
    st.session_state['get_filtered_profiles_button'] = 1

if st.session_state['get_filtered_profiles_button']:
    df = pd.read_excel("./data/technical_filtered.xlsx")
    st.dataframe(df[["Applicant_Name","years_of_exp","Key_Skills","Linkedin_Profile","GitHub_Profile","Mail_Id"]], width=1000)



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
    matching_profiles = pd.read_excel("./data/technical_filtered.xlsx")
    for i in range(matching_profiles.shape[0]):
        email = matching_profiles.loc[i,"Mail_Id"]
        candidate_name = matching_profiles.loc[i,"Applicant_Name"]
        val = send_mail(reciever_mail=email,job_position=job_position,candidate_name=candidate_name,HR_Name=HR_Name,test_link=test_link)

    print("Successfully sent mail to all the Potential Candidates ")

