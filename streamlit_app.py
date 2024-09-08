# Må bruke følgende kommando for å starte programmet: streamlit run streamlit_app.py --server.enableCORS false --server.enableXsrfProtection false


import pandas as pd
import streamlit as st
import openpyxl
import plotly.graph_objects as go
st.set_page_config(layout="wide", page_title="Regular Plot")



wb = openpyxl.load_workbook("Maria H-2 Pressure Tests.xlsx")



## Select sheet
sheet_selector = st.sidebar.selectbox("Select data to plot:",wb.sheetnames)     
df = pd.read_excel("Maria H-2 Pressure Tests.xlsx",sheet_selector, index_col=0)
st.markdown(f"### Selected: `{sheet_selector}`")


f = go.FigureWidget()
colors = ["red", "LightCoral", "CornflowerBlue", "blue","grey","grey","grey","grey", "grey", "grey", "grey", "grey", "grey", "grey", "grey"]



i=0
for c in df.columns:
    f.add_trace(
        go.Scatter(
            x=df.index,  # construct list of identical X values to match the Y-list
            y=df[c],  # Your MTU list
            mode='lines',  # scatter plot without lines
            marker=dict(
                color=colors[i],  # set color by the value of Y
                ),
                name=c,
            )
            )
    i = i+1
f.update_layout(height=700, xaxis_tickfont_size=16, yaxis_tickfont_size=16, xaxis_tickfont_color="black", yaxis_tickfont_color="black")


st.plotly_chart(f, use_container_width=True)
