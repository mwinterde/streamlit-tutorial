import streamlit as st

def write():
    st.title("Streamlit")
    st.header("Was ist Streamlit?")
    col1, col2 = st.beta_columns([1, 6])
    col1.image("resources/streamlit.png", width=80)
    col2.subheader("Streamlit ist ein schneller Weg um Daten Apps zu bauen")
    st.markdown(
        """
        > Streamlit is fastest way to build and share data apps.\n
        > Streamlit turns data scripts into shareable web apps in minutes.
        > All in Python. All for free. No front‑end experience required.
        """)
    st.header("Warum Streamlit?")
    st.subheader("Es geht wirklich schnell")
    st.image("resources/bolt1.jpg", width=400)
    st.subheader("Du musst wirklich nichts über Frontend wissen")
    st.image("resources/frontend.jpg", width=400)
    st.subheader("Python")
    st.image("resources/python.png", width=400)
    st.subheader("Besserer Code")
    st.image("resources/cleancode.jpg", width=400)
    st.header("Warum nicht Streamlit?")
    st.subheader("Streamlit ist noch jung")
    st.image("resources/history.png", width=400)
    st.subheader("Die Usability kommt nicht umsonst")
    st.image("resources/tradeoff.jpg", width=400)