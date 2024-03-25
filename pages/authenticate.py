import streamlit as st
import os
import pyrebase
from menu import menu

if "role" not in st.session_state:
    st.session_state.role = None


st.set_page_config(page_title="Login/Signup", page_icon="🦙")
menu()


firebaseConfig = {
  'apiKey': "AIzaSyB1bstaExh83Azyr190rdC00M-RZGCEvgk",
  'authDomain': "testproject-cb717.firebaseapp.com",
  'projectId': "testproject-cb717",
  'storageBucket': "testproject-cb717.appspot.com",
  'messagingSenderId': "513075433545",
  'appId': "1:513075433545:web:eee7fd4eb6c708ef93ef98",
  'measurementId': "G-G68Z9SSZ4T",
  'databaseURL': ''
  }

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()

def signup(email,password):
    if auth.get_account_info(email):
        return "User already exists"
    else:
        user = auth.create_user_with_email_and_password(email, password)
        return user

def login(email,password):
    try:
        user = auth.sign_in_with_email_and_password(email, password)
        st.success("Successfully Logged In")
        return user
    except:
        return "Invalid Credentials"

type = st.selectbox("Sign Up/Log In", ["Sign Up", "Log In"])
if type == "Log In":
    st.header("Login")
    email = st.text_input("Email")
    password = st.text_input("Password", type='password')
    login_button = st.button("Login")
    if login_button:
        user = login(email,password)
        if user == "Invalid Credentials":
            st.error("Invalid Credentials")
        else:
            st.success("Successfully Logged In")
            st.session_state.role = user['email']
            st.switch_page("./pages/project.py")
if type == "Sign Up":
    st.header("Sign Up")
    email = st.text_input("Email")
    password = st.text_input("Password", type='password')
    signup_button = st.button("Sign Up")
    if signup_button:
        user = signup(email,password)
        if user == "User already exists":
            st.error("User already exists")
        else:
            st.success("Successfully Signed Up")
            st.session_state.role = user['email']
            st.switch_page("./pages/project.py")







    


