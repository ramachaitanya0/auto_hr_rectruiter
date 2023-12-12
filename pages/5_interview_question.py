import streamlit as st
from langchain.chat_models import  AzureChatOpenAI
from langchain.callbacks import get_openai_callback
from dotenv import  load_dotenv
load_dotenv()

if "Amount_Spent" not in st.session_state :
    st.session_state["Amount_Spent"] = 0.0

st.header("Get Question and Answers",divider='rainbow')
qa_input =  st.text_input(label="Get Q&A")
jd_button = st.button("Submit")


if jd_button :
    with get_openai_callback() as cr :
        model = AzureChatOpenAI()
        val = model.invoke(qa_input, engine="gpt_4_32k")
        st.session_state.Amount_Spent += cr.total_cost

    st.write(val.content)


