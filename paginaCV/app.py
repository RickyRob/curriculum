import streamlit as st
import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html, Input, Output
import yfinance as yf
import numpy as np
import plotly.graph_objects as go


# Configuración de la página
st.set_page_config(page_title="Portafolio", layout="wide")

# Sidebar de navegación
st.sidebar.title("📁 Información")
opcion = st.sidebar.radio("Ir a:", ["🏠 Inicio", "📄 Currículum", "📊 Dashboards", "🛠️ Proyectos"])

# Inicio
if opcion == "🏠 Inicio":
    st.title("👋 ¡En esta página encontrarás más sobre mí!")
    st.markdown("""
        <p style='text-align: justify; font-size: 20px; padding-left: 70px; padding-right:80px; padding-top: 70'>
        En este espacio que he creado podrás encontrar un poco más sobre mi experiencia profesional 
        a lo largo de estos años en los cuales he tenido la gran fortuna de establecer lazos con 
        las compañias más importantes del sector financiero y comercial.
        </p>
        """, unsafe_allow_html=True)
    
    html_lista = """
        <ul style="font-size:20px;padding-left: 70px;font-weight:bold;">
            <li>BBVA Corporate Investment Banking: Analista de CIB</li>
            <li>IDS Comercial BBVA: Analista de Datos</li>
            <li>WALMART: Analista Financiero y de Pronósticos</li>
        </ul>
        """

    st.markdown(html_lista, unsafe_allow_html=True)
    st.markdown("""
        <p style='text-align: justify; font-size: 20px; padding-left: 70px; padding-right:80px; padding-top: 70'>
        En cada compañía he logrado establecer logros y metas resaltando la adaptación y el  sentido 
        de urgencia que cada proyecto demandaba pero sin perder de vista la calidad de los entregables.
        </p>
        """, unsafe_allow_html=True)
    st.markdown("""
        <p style='text-align: justify; font-size: 20px; padding-left: 70px; padding-right:80px; padding-top: 70'>
        Mi enfoque esta en los Pronósticos y Análisis Financiero con metodologías de procesos estocásticos, 
        uso de tecnólogias como Python, Spark y SQL.
        </p>
        """, unsafe_allow_html=True)
    

# Currículum
elif opcion == "📄 Currículum":
    st.title("📄 Mi Currículum")
    st.write("Puedes descargar mi CV en PDF aquí:")
    with open("paginaCV/cv.pdf", "rb") as file:
    #with open("cv.pdf", "rb") as file:
        st.download_button("📥 Descargar CV", file, "cv.pdf", mime="application/pdf")
   

# Dashboards
elif opcion == "📊 Dashboards":

    #st.title("📈 Precio de Activos Financieros")

    # Cargar tickers del Nasdaq
    url = "https://datahub.io/core/nasdaq-listings/r/nasdaq-listed.csv"
    df = pd.read_csv(url)
    tickers = df['Symbol'][:-2].tolist()

    # Selección de ticker
    ticker = st.selectbox("Selecciona un ticker", tickers, index=tickers.index("AAPL") if "AAPL" in tickers else 0)

    # Descargar datos del ticker
    data = yf.download(ticker, period='2y')
    data = data.stack()
    if data.empty:
        st.warning("No se encontraron datos para este ticker.")
    else:
        # 📈 Gráfico de precio
        data = data.reset_index()

        fig_precio = px.line(data, x='Date', y='Close',
                             title=f"Precio de cierre de {ticker}")
        st.plotly_chart(fig_precio, use_container_width=True)

        # Crear columnas
        col1, col2 = st.columns(2)



        ############### HISTOGRAMA
        with col1:
            # 📊 Histograma de rendimientos diarios
            data['Rendimientos'] = data['Close'].pct_change()
            data = data.dropna()

            fig_hist = px.histogram(data, x='Rendimientos', nbins=60,
                                    title=f"Histograma de Rendimientos Diarios de {ticker}",
                                    labels={'Rendimientos': 'Rendimiento (%)'})
            st.plotly_chart(fig_hist, use_container_width=True)

        ##############TACOMETRO
        with col2:
            vol = data["Close"].std()
            medio = data["Close"].mean()
            precio_actual = data["Close"].iloc[-1]
            
            # Definir la posición de la aguja
            if precio_actual < -1.5 * vol + medio:
                valor_gauge = -0.5
            elif precio_actual < 1.5 * vol + medio:
                valor_gauge = 0.5
            else:
                valor_gauge = 0
            

            fig = go.Figure(go.Indicator(
                mode="gauge+number",
                value=valor_gauge,
                #number={'suffix': " pos"},
                title={'text': f"Oportunidad {ticker}"},
                gauge={
                    'axis': {'range': [-1, 1]},
                    'bar': {'color': "darkblue"},
                    'steps': [
                        {'range': [-1, -0.5], 'color': "red"},
                        {'range': [-0.5, 0.5], 'color': "orange"},
                        {'range': [0.5, 1], 'color': "green"},
                    ],
                    'threshold': {
                        'line': {'color': "black", 'width': 4},
                        'thickness': 0.75,
                        'value': valor_gauge
                    }
                }
            ))

            st.plotly_chart(fig, use_container_width=True)


# Proyectos
elif opcion == "🛠️ Proyectos":
    st.title("🛠️ Mis Proyectos")
    st.write("""
    Aquí puedes encontrar algunos de los proyectos en los que he trabajado:
    
    - 📊 **Análisis de ventas:** Análisis de ventas y proyecciones con métodos estocásticos.
    - 📊 **Construcción de Dashboards:** Construcción de Indicadores de Eficiencia.
    - 🤖 **Pronósticos Bursátiles:** Construcción de Modelos AR, MA, ARMA y Machine Learning.
    - 🌐 **Análista de Datos:** Ingeniero de Datos para Proyectos Clientes Institucionales.
    - 📈 **Predicción de Precios:** Modelos de Medias Móviles, Suavización Exponencial y Machine Learning.
    - 📈 **Análisis Financiero:** Anáilisis de Estados Financieros.
    """)

    st.info("¿Te gustaría ver algún proyecto en detalle? ¡Contáctame: 5518383876 o E-Mail: ingrscfi@gmail.com!")

