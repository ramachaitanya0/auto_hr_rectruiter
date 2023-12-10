import pandas as pd
import streamlit as st


def dataframe_with_selections(df):
    df_with_selections = df.copy()
    df_with_selections.insert(0, "Select", False)

    # Get dataframe row-selections from user with st.data_editor
    edited_df = st.data_editor(
        df_with_selections,
        hide_index=True,
        column_config={"Select": st.column_config.CheckboxColumn(required=True)},
        disabled=df.columns,
    )

    # Filter the dataframe using the temporary column, then drop the column
    selected_rows = edited_df[edited_df.Select]
    return selected_rows.drop('Select', axis=1)

st.header("Matching Profiles",divider='rainbow')

submit = st.button("Get Matching Profiles")

if "get_matching_profiles_button" not in st.session_state :
    st.session_state['get_matching_profiles_button'] = 0

if submit :
    st.session_state['get_matching_profiles_button'] = 1

if st.session_state['get_matching_profiles_button']:
    df = pd.read_csv("data/matching_profiles.csv")
    selection = dataframe_with_selections(df)
    st.write("Select the Applicatnts:")
    st.dataframe(selection)






