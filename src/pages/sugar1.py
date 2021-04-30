import streamlit as st
import numpy as np 
import pandas as pd
import altair as alt
import plotly.figure_factory as ff

def write():
    st.title("Streamlit Sugar")

    # Text darstellen
    st.header("Text darstellen")

    st.subheader("Einfacher Text")
    with st.echo():
        st.text("Das ist ein einfacher Text")

    st.subheader("Markdown")
    with st.echo():
        st.markdown("Das ist ein __Mark*down* Text__")

    st.subheader("Latex")
    with st.echo():
        st.latex(r"a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} = \sum_{k=0}^{n-1} ar^k")
    
    st.subheader("Code")
    with st.echo():
        st.code("a = np.random.randn(100)", language='python')
    with st.echo():
        st.code("ssh -i ~/.ssh/keyfile user@hostname", language='bash')

    # Daten darstellen
    st.header("Daten darstellen")

    st.subheader("Tabellen")
    with st.echo():
        df = pd.DataFrame(np.random.randn(5, 3), columns=['a', 'b', 'c'])
        st.table(df)

    st.subheader("Gestylte Tabellen")
    with st.echo():
        def colormap(val):
            color = "#de796e" if val<0 else "#5eae76"
            return f"background-color: {color}"
        st.table(df.style.applymap(colormap).format("{:.2f}"))
    
    st.subheader("JSON")
    with st.echo():
        st.json({'a': 'foo', 'b': 'bar', 'c': ['stuff', 'like', 'this']})

    # Daten visualisieren
    st.header("Daten visualisieren")

    st.subheader("Altair")
    with st.echo():
        st.line_chart(df)
    with st.echo():
        st.area_chart(df)
    with st.echo():
        st.bar_chart(df)
    
    st.subheader("Plotly")
    with st.echo():
        x1 = np.random.randn(1000) - 2
        x2 = np.random.randn(1000) 
        x3 = np.random.randn(1000) + 2
        fig = ff.create_distplot([x1, x2, x3], ['a', 'b', 'c'])
        st.plotly_chart(fig, use_container_width=True)
    
    st.subheader("Maps")
    with st.echo():
        coords = [50.93, 6.95] + np.random.randn(100, 2) / [50, 50]
        df = pd.DataFrame(coords, columns = ['lat', 'lon'])
        st.map(df)