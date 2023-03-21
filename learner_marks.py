import openpyxl
import streamlit as st

# Load the data

excel_file = "student_marks.xlsx"
workbook = openpyxl.load_workbook(excel_file)
worksheet = workbook.active

# Set up the Streamlit app
st.title("Learner Marks Lookup")

# Add input fields for name and password
name = st.text_input("Name:")
password = st.text_input("Password:", type="password")

# Add a button to submit the inputs
if st.button("Submit"):
    # Check if the name and password match any rows in the worksheet
    match = None
    for row in worksheet.iter_rows(min_row=2):
        if row[0].value == name and row[1].value == password:
            match = row
            break

    if match is not None:
        # Display the learner's mark
        mark = match[2].value
        st.success(f"Your mark is {mark}.")
    else:
        # Display an error message if the name and password don't match any rows
        st.error("Invalid name or password.")

