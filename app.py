import streamlit as st

# Read your HTML file
with open("index.html", "r") as file:
    html_content = file.read()

# Display the HTML inside Streamlit
st.components.v1.html(html_content, height=800, scrolling=True)
