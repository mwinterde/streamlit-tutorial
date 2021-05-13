import streamlit as st


def write():
    st.title("Tutorial")

    # Voraussetzungen
    st.header("Voraussetzungen")
    st.markdown("""* Python 3.8
* Google Cloud SDK
* Docker
"""
)

    st.header("Ausblick Ordnerstruktur")
    st.code(""".
├── venv/               # Virtuelle Umgebung für lokale Entwicklung
├── app.py              # Quellcode für die Streamlit App
├── Dockerfile          # Liste von Anweisungen zur Erstellung eines Docker Image
└── requirements.txt    # Eingefrorene Python Abhängigkeiten
"""
)

    st.header("Virtuelle Umgebung für lokale Entwicklung einrichten")
    st.markdown("Virtuelle Umgebung erstellen")
    st.code("python3 -m venv venv", language="bash")
    st.markdown("Virtuelle Umgebung aktivieren")
    st.code("source venv/bin/activate", language="bash")
    st.markdown("Abhängigkeiten installieren")
    st.code("pip3 install streamlit pandas numpy")

    st.header("Lokale Entwicklung der Streamlit App")
    st.markdown("Erste Version von `app.py` erstellen")
    st.code("""import streamlit as st
import numpy as np
import pandas as pd

def main():
    st.title("Hello World :wave:")

if __name__ == '__main__':
    main()
"""
)
    st.markdown("Streamlit App starten")
    st.code("streamlit run app.py")
    st.markdown("App Entwicklung im Splitscreen Modus :fire:")
    st.image("resources/splitscreen.png")
    st.markdown("Erweiterung um Dummy Tabelle und Chart")
    st.code("""import streamlit as st
import numpy as np
import pandas as pd

def main():
    st.title("Hello World :wave:")
    df = pd.DataFrame(
        data=np.random.randn(10, 3), 
        columns=['a', 'b', 'c']
    )
    st.write(df)
    st.line_chart(df)

if __name__ == '__main__':
    main()
"""
)
    st.image("resources/finalapp.png")

    st.header("Docker Image bauen und testen")
    st.markdown("Abhängigkeiten einfrieren")
    st.code("pip3 freeze > requirements.txt")
    st.markdown("Dockerfile erstellen")
    st.code("""FROM python:3.8-slim-buster
COPY requirements.txt .
RUN pip3 install --upgrade pip && pip3 install -r requirements.txt 
COPY app.py .
EXPOSE 8501
CMD streamlit run app.py 
""", language = "docker"
)
    st.markdown("Docker Image bauen")
    st.code("docker build -t [IMAGE_NAME]:latest .")
    st.markdown("Docker Container in lokaler Umgebung testen")
    st.code("docker run -d --name [CONTAINER_NAME] -p 8501:8501 [IMAGE_NAME]")
    st.markdown("Docker Container stoppen")
    st.code("docker stop [CONTAINER_NAME]")

    st.header("App mit Google Cloud Run deployen")
    st.markdown("Docker Image in Container Registry hochladen")
    st.code("gcloud build submit -t eu.gcr.io/[PROJECT_ID]/[IMAGE_NAME]:latest")
    st.markdown("Cloud Run Service erstellen")
    st.code("gcloud run deploy --image eu.gcr.io/[PROJECT_ID]/[IMAGE_NAME]:latest --platform managed")

    st.header("Fertig :tada:")
