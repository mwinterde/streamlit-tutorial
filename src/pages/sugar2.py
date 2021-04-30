import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

def write():
    st.title("Mehr Streamlit Sugar")

    # Widgets
    st.header("Widgets")

    st.subheader("Button")
    with st.echo():
        if st.button("Start"):
            st.write("Gestartet")
    
    st.subheader("Checkbox")
    with st.echo():
        agree = st.checkbox("Einverstanden?")
        st.write("Ja" if agree else "Nein")
    
    st.subheader("Slider")
    with st.echo():
        number = st.slider("Deine Nummer", 0, 100)
        st.write("Deine Nummer lautet %d" % number)
    
    st.subheader("Selectbox")
    with st.echo():
        options = ['Option A', 'Option B', 'Option C']
        choice = st.selectbox("Deine Auswahl", options)
        st.write("Deine Auswahl lautet %s" % choice)
    
    st.subheader("Multiselect")
    with st.echo():
        options = ['Option A', 'Option B', 'Option C']
        choices = st.multiselect("Deine Auswahl", options)
        st.write("Deine Auswahl lautet %s" % ", ".join(choices))
    
    st.subheader("Input Felder")
    with st.echo():
        st.text_input("Text Input")
        st.number_input("Number Input")
        st.date_input("Date Input")
    
    st.subheader("File Uploader")
    with st.echo():
        data_file = st.file_uploader("File Uploader", type="csv")
        if data_file:
            df = pd.read_csv(data_file)
            st.write(df)
    
    # Layouting
    st.header("Layouting")
    
    st.subheader("Spalten")
    with st.echo():
        col1, col2, col3 = st.beta_columns(3)
        with col1:
            st.header("Katze")
            st.image("https://static.streamlit.io/examples/cat.jpg")
        with col2:
            st.header("Hund")
            st.image("https://static.streamlit.io/examples/dog.jpg")
        with col3:
            st.header("Eule")
            st.image("https://static.streamlit.io/examples/owl.jpg")
    
    st.subheader("Container")
    with st.echo():
        with st.beta_expander("Das ist ein Container"):
            st.write("Hier könnte ein sehr langer Text stehen")
            st.write("Oder Daten?")
            df = pd.DataFrame(np.random.randn(10, 3), columns=list('abc'))
            st.write(df)