import streamlit as st
import requests

# Configuración de la página
st.set_page_config(page_title="Predicción de Churn", page_icon="📉", layout="centered")

# Título principal
st.title("📉 Simulador de Retención de Clientes")
st.markdown("Ingresa los datos del cliente para evaluar su riesgo de fuga mediante Machine Learning.")
st.divider()

# Formularios de entrada de datos (Columnas para que se vea ordenado)
col1, col2 = st.columns(2)

with col1:
    antiguedad = st.slider("Antigüedad (Meses)", min_value=1, max_value=72, value=12)
    cargo = st.number_input("Cargo Mensual ($ USD)", min_value=10.0, max_value=150.0, value=50.0)

with col2:
    reclamos = st.number_input("Reclamos Previos", min_value=0, max_value=10, value=0)
    contrato = st.selectbox("Tipo de Contrato", ["Mes a mes", "Un año", "Dos años"])

st.divider()

# Botón de acción
if st.button("🔮 Predecir Riesgo de Fuga", use_container_width=True):
    
    # Preparamos los datos tal como los pide tu API
    datos_cliente = {
        "antiguedad_meses": antiguedad,
        "cargo_mensual": cargo,
        "reclamos_previos": reclamos,
        "tipo_contrato": contrato
    }
    
    # Hacemos la llamada a tu contenedor Docker que está corriendo de fondo
    try:
        respuesta = requests.post("https://api-churn-carlo.onrender.com", json=datos_cliente)
        
        if respuesta.status_code == 200:
            resultado = respuesta.json()
            
            # Mostramos los resultados visualmente
            st.subheader("Resultados del Modelo:")
            
            if resultado["alerta_fuga"]:
                st.error(f"¡ALERTA! Alto riesgo de fuga.")
                st.metric(label="Probabilidad de Abandono", value=resultado["probabilidad_abandono"])
                st.info(f"Sugerencia: {resultado['accion_sugerida']}")
            else:
                st.success(f"Cliente estable. Bajo riesgo de fuga.")
                st.metric(label="Probabilidad de Abandono", value=resultado["probabilidad_abandono"])
                
        else:
            st.error("Error en la API. Revisa que tu contenedor de FastAPI esté corriendo.")
            
    except requests.exceptions.ConnectionError:
        st.error("No se pudo conectar con la API. ¿Aseguraste que el contenedor en el puerto 8000 está encendido?")