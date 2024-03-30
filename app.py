import streamlit as st
import os

from menu import menu
# projects
# menu()


if __name__ == "__main__":
    st.set_page_config(page_title="DocQA Pro", page_icon="🦙")


    # Page Title and Description
    st.title("Welcome to :rainbow[DocQA Pro]!")
    st.write("Your premier destination for seamless document question answering. Empowering you with the answers you need, right at your fingertips.")

    # Our Description
    st.header("About Us")
    st.write("""
    At DocQA Pro, we revolutionize the way you interact with documents. Gone are the days of tedious manual searching through pages of text. Our cutting-edge technology leverages the power of natural language processing to swiftly provide accurate answers to your questions, transforming the way you work and learn.
    """)

    # Our Process
    st.header("Our Process")
    st.write("""
    1. **Upload Your Document**: Simply upload your document to our platform. We support various file formats including PDF, DOCX, and TXT.
    2. **Ask Your Questions**: Pose your questions to our advanced question answering system.
    3. **Get Instant Answers**: Sit back and relax as our system swiftly scans through your document and provides you with precise answers in seconds.

    Our process is designed to be seamless, efficient, and tailored to meet your specific needs, saving you valuable time and effort.
    """)

    # Our Targets
    st.header("Our Targets")
    st.write("""
    - **Professionals**: Enhance productivity and streamline workflow by quickly accessing vital information within documents.
    - **Students**: Simplify research tasks and accelerate learning with instant access to answers from academic materials.
    - **Researchers**: Expedite data extraction and analysis processes, enabling faster insights and breakthroughs.

    No matter your field or profession, DocQA Pro is your trusted partner in unlocking the wealth of knowledge hidden within your documents.
    """)

    # Get Started Section
    st.header("Get Started")
    st.write("""
    Ready to experience the future of document interaction? Sign up now and join countless others who have embraced the power of DocQA Pro!
    """)
    if st.button("Sign Up Now"):
        # Redirect to the sign-up page or any desired page
        st.write("Redirecting you to the sign-up page...")
        st.switch_page("./pages/authenticate.py")
        # You can add redirection code here

    # Footer
    st.markdown("""
    ---
    Experience the future of document interaction with DocQA Pro. Simplify, streamline, and succeed.
    """)


    menu()
