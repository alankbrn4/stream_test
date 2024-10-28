import streamlit as st
import pandas as pd
import numpy as np

# Configuración básica de la página
st.set_page_config(
    page_title="Monitor Industrial",
    page_icon="🏭",
    layout="wide"
)

# Título principal
st.title("Sistema de Monitoreo Industrial")
st.write("Bienvenido al sistema de monitoreo en tiempo real")

# Diferentes tipos de textos
st.header("Panel Principal")
st.subheader("Datos del Sensor")
st.text("Información en texto plano")
st.markdown("**Texto con formato Markdown**")

# Widgets básicos
temperatura = st.slider("Temperatura", min_value=0, max_value=100, value=25)

# Columnas
col1, col2 = st.columns(2)
with col1:
    st.metric("Temperatura", f"{temperatura}°C", delta="1.2°C")
with col2:
    st.metric("Presión", "1013 hPa", delta="-2 hPa")
