import streamlit as st

import src.pages.welcome
import src.pages.streamlit
import src.pages.cloudrun
import src.pages.sugar1
import src.pages.sugar2
import src.pages.tutorial



PAGES = {
    "Willkommen": src.pages.welcome,
    "Streamlit?": src.pages.streamlit,
    "Cloud Run?": src.pages.cloudrun,
    "Streamlit Sugar": src.pages.sugar1,
    "Mehr Streamlit Sugar": src.pages.sugar2,
    "Tutorial": src.pages.tutorial
}


def main():

    st.set_page_config(page_title='Streamlit Tutorial')
    st.sidebar.title("Navigation")
    page_options = list(PAGES.keys())
    selection = st.sidebar.radio('Gehe zu', page_options)
    page = PAGES[selection]
    page.write()

    st.sidebar.title("Kontakt")
    st.sidebar.info(
"""Diese Seite befindet sich im Aufbau. Wenn ihr Fehler entdeckt
oder Verbesserungsvorschläge habt, freue ich mich über eine kurze
Rückmeldung bei [GitHub](https://github.com/rewe-digital-analytics/ds-streamlit-tutorial/issues) 
oder [per Mail](mailto:mw210992@gmail.com).
""")


if __name__ == '__main__':
    main()