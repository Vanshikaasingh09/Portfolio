<<<<<<< HEAD
import streamlit as st

# Read your HTML file
with open("index.html", "r") as file:
    html_content = file.read()

# Display the HTML inside Streamlit
st.components.v1.html(html_content, height=800, scrolling=True)
=======
import streamlit as st

# Read your updated HTML file
with open("index.html", "r", encoding='utf-8') as file:
    html_content = file.read()

# Display the HTML inside Streamlit
st.components.v1.html(html_content, height=1000, scrolling=True)
>>>>>>> 2d6bd53 (changes)
