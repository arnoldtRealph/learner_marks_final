import pandas as pd
import streamlit as st



# Load the data
data_folder = "data/"
excel_file = "student_marks.xlsx"
df = pd.read_excel(excel_file)

# Set up the Streamlit app
st.title("Learner Marks Lookup")

# Add input fields for name and password
name = st.text_input("Name:")
password = st.text_input("Password:", type="password")

# Add a button to submit the inputs
if st.button("Submit"):
    # Check if the name and password match any rows in the dataframe
    match = df[(df['Name'] == name) & (df['Password'] == password)]
    if not match.empty:
        # Display the learner's mark
        mark = match.iloc[0]['Marks']
        st.success(f"Your mark is {mark}.")
    else:
        # Display an error message if the name and password don't match any rows
        st.error("Invalid name or password.")
