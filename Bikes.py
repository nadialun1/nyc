#Rodrigo Hernández A01610903
#Nadia Luna Rivas A01658134
# Carlos Ledezma A00828114 


#-----------Librerías
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt

#-----------Constantes y datos
nameC = "citibike-tripdata.csv"
nrowsC = 1000

sidebar = st.sidebar

titleS = 'Recorridos en bicicleta'



#-----------Funciones
@st.cache(suppress_st_warning=True)
def showDataset(name,nrows):
    df=pd.read_csv(name,nrows=nrows)
    df['horas'] = (pd.to_datetime(df['started_at'])).dt.hour
    df.rename(columns = {'start_lat': 'lat', 'start_lng': 'lon'}, inplace = True)
    dfvis = df.copy()
    return df, dfvis

df, dfvis= showDataset(nameC,nrowsC)

#----------Sidebar
sidebar.title(titleS)

if sidebar.checkbox('Visualizar Dataset?'):
    st.dataframe(dfvis)

optionals = sidebar.expander('Escoger una hora',True)
horFil = optionals.slider(
    'Hora',
    min_value= int(df['horas'].min()),
    max_value= int(df['horas'].max())
)

#y = df.groupby('')

f1 = px.bar(df, x= df['horas'].unique(), y=df['horas'].value_counts(), labels = dict(y = 'Recorridos', x = 'Horas'), title = 'Recorridos por hora')
st.plotly_chart(f1)

data_vis = df[(df['horas'] == horFil)]
st.header(f'Mapa de recorridos en bici a las {horFil}:00 horas')
st.map(data_vis)


