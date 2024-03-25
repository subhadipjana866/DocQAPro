import streamlit as st


def authmenu():
    st.sidebar.page_link("./pages/project.py",label="Projects")
    st.sidebar.page_link("./pages/query.py",label="Query")
    
    # st.switch_page("./pages/project.py")

def unauthmenu():
    st.sidebar.page_link("./pages/authenticate.py",label="Login/Signup")
    # st.switch_page("./pages/authenticate.py")
    


def menu():

    if "role" not in st.session_state or st.session_state.role is None:
        unauthmenu()
    else:
        authmenu()
        logout = st.sidebar.button("Logout")
        if logout:
            st.session_state.role = None
            st.session_state.projects = []
            st.session_state.curr = None
            st.session_state.messages = []
            st.session_state.clear()
            st.switch_page("./pages/authenticate.py")
    
        
    