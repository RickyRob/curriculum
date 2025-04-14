import streamlit as st
import pandas as pd
import plotly.express as px

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
        st.download_button("📥 Descargar CV", file, "cv.pdf", mime="application/pdf")
   

# Dashboards
elif opcion == "📊 Dashboards":
    st.title("📊 Dashboards Interactivos")
    df = pd.DataFrame({
        'Categoría': ['A', 'B', 'C', 'D'],
        'Valor': [100, 200, 150, 300],
        'Mes': ['Enero', 'Febrero', 'Marzo', 'Abril']
    })

    col1, col2 = st.columns([2, 1])

    with col1:
        st.subheader("📈 Gráfico Principal")
        fig1 = px.line(df, x='Mes', y='Valor', title="Tendencia Mensual")
        st.plotly_chart(fig1, use_container_width=True)

    with col2:
        st.subheader("📊 Gráfico Secundario 1")
        fig2 = px.bar(df, x='Categoría', y='Valor', title="Valores por Categoría")
        st.plotly_chart(fig2, use_container_width=True)

        st.subheader("📉 Gráfico Secundario 2")
        fig3 = px.pie(df, names='Categoría', values='Valor', title="Distribución por Categoría")
        st.plotly_chart(fig3, use_container_width=True)

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

