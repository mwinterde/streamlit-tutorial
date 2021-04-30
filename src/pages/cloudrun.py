import streamlit as st

def write():
    st.title("Google Cloud Run")
    st.header("Was ist Google Cloud Run?")
    col1, col2 = st.beta_columns([1, 6])
    col1.image("resources/cloudrun.png", width=80)
    col2.subheader("Google Cloud Run ist ein schneller Weg um Container bereitzustellen")
    st.markdown(
        """
        > Container to production in seconds. Google Cloud Run allows you to 
        > develop and deploy highly scalable containerized applications on a 
        > fully managed serverless platform.
        """)
    st.header("Warum Google Cloud Run?")
    st.subheader("Es geht wirklich schnell")
    st.image("resources/bolt2.jpg", width=400)
    st.subheader("Vollständig verwaltet")
    st.image("resources/relax.jpg", width=400)
    st.subheader("Docker")
    st.image("resources/docker.png", width=400)
    st.subheader("Pay Per Use")
    st.image("resources/saving.jpg", width=400)
    st.header("Warum nicht Google Cloud Run?")  
    st.subheader("Cold Starts mit langen Antwortzeiten")
    st.image("resources/wakeup.gif", width=400)