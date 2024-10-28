import streamlit as st
import random
import time

class SensorTemperatura:
    def __init__(self):
        self.valor_base = 25
        
    def leer(self):
        # Simulamos variación aleatoria
        return self.valor_base + random.uniform(-5, 5)

# Creamos instancia del sensor
sensor = SensorTemperatura()

# Contenedor para gráfica en tiempo real
grafica = st.empty()

# Botón para iniciar monitoreo
if st.button("Iniciar Monitoreo"):
    for i in range(10):
        temperatura = sensor.leer()
        grafica.metric(
            "Temperatura Actual",
            f"{temperatura:.1f}°C",
            f"{temperatura - 25:.1f}°C"
        )
        time.sleep(1)
