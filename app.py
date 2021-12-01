import string
import random
import streamlit as st

hide_st_style = """
        <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        button[title="View fullscreen"] {
        display: none;
        }

        button[title="View fullscreen"]:hover {
        display: none;
        }
        </style>
        """
st.markdown(hide_st_style, unsafe_allow_html=True)


s1 = list(string.ascii_lowercase)
s2 = list(string.ascii_uppercase)
s3 = list(string.digits)
s4 = list(string.punctuation)

int_input = st.slider('Characters for the password', min_value=6, max_value=50, value=10, step=1)

random.shuffle(s1)
random.shuffle(s2)
random.shuffle(s3)
random.shuffle(s4)

part1 = round(int_input * (30/100))
part2 = round(int_input * (20/100))

password = []

for i in range(part1):
    password.append(s1[i])
    password.append(s2[i])

for i in range(part2):
    password.append(s3[i])
    password.append(s4[i])

password = "".join(password[0:])

st.write("Generate Strong Password")
st.code(password)
