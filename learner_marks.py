import openpyxl
import streamlit as st

st.set_page_config(page_title= "My Webpage", page_icon=":tada:", layout= "wide")
# Load the data

excel_file = "student_marks.xlsx"
workbook = openpyxl.load_workbook(excel_file)
worksheet = workbook.active

# Set up the Streamlit app
st.title("TEGNIESE WETENSKAPPE MAART 2023")

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
        st.success(f"JY HET {mark} BEHAAL.")
    else:
        # Display an error message if the name and password don't match any rows
        st.error("Invalid name or password.")

with st.container():
    st.write("---")

st.title("Geluk aan die volgende Graad 12 leerders!")
st.subheader("Hulle het die beste gevaar in die Maart Toets:")
st.header(" 1. Shashmica Springbok 2. Gerath Du Raan 3. Elmar Eiman")
st.write("Julle maak my trots. Hou so aan!")

