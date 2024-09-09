import streamlit as st
import plotly.graph_objects as go
st.set_page_config(layout="wide", page_title="Regular Plot")



st.sidebar.header("Please input parameters")
## input volume
volume = st.sidebar.number_input("Volume of the pressurized system[m3]")

## start pressure
start_pressure = st.sidebar.number_input("Start pressure [bar]")
## end pressure
end_pressure = st.sidebar.number_input("End pressure [bar]")

## input DP at surface
diffpressure = st.sidebar.number_input("Diffpressure of the system[bar]")
## Select compressibility
compressibility = st.sidebar.selectbox("Select fluid", ["Base oil", "Sea Water", "Brine"])
## Input time interval
time = st.sidebar.number_input("Time interval [minutes]")

#TODO Add leak rate calculation
leakrate = 100

st.header("Leak rate criteria")
st.text("Leak rate is: "+str(leakrate) + " liter/min")