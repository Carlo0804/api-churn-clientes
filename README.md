# 📉 Sistema Predictivo de Retención de Clientes (Customer Churn)

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://api-churn-clientes-nbcjsbctduudracyaffl4k.streamlit.app/)
[![API Docs](https://img.shields.io/badge/API_Docs-Swagger_UI-85EA2D?logo=fastapi)](https://api-churn-carlo.onrender.com/docs)

## 📌 El Problema de Negocio
En la industria de telecomunicaciones, el costo de adquirir un cliente nuevo es mucho mayor que el de retener uno existente. Este proyecto es una solución end-to-end de Machine Learning diseñada para identificar clientes con alto riesgo de abandono (Churn), traduciendo predicciones matemáticas en decisiones de negocio accionables (como ofrecer descuentos automáticos de retención).

## 🏗️ Arquitectura del Sistema (Microservicios)
Este proyecto fue diseñado con una arquitectura desacoplada para garantizar escalabilidad y replicabilidad en entornos de producción:

*   **🧠 Modelo ML:** Entrenamiento de un `RandomForestClassifier` y pipelines de preprocesamiento (`Scikit-Learn`, `Pandas`).
*   **⚙️ Backend (API):** Microservicio construido con `FastAPI` (Python 3.11), empaquetado en un contenedor de `Docker` y desplegado en la nube a través de **Render**.
*   **🎨 Frontend (UI):** Aplicación web interactiva desarrollada con `Streamlit`. Desplegada y conectada a la API pública mediante **Streamlit Community Cloud**.

## 🛠️ Stack Tecnológico
*   **Lenguaje:** Python 3.11
*   **Data Science:** Scikit-Learn (v1.9.0), Pandas, NumPy, Joblib.
*   **Ingeniería & Despliegue (MLOps):** FastAPI, Docker, Uvicorn, Streamlit, Render.
*   **Entorno de Desarrollo:** Linux (Ubuntu).

## 🚀 Pruebas en Vivo (Live Demo)
Puedes interactuar con el modelo directamente desde tu navegador sin instalar nada:
1. **[Simulador Web (Streamlit)](https://api-churn-clientes-nbcjsbctduudracyaffl4k.streamlit.app/):** Interfaz visual para evaluar clientes.
2. **[Documentación API (Swagger UI)](https://api-churn-carlo.onrender.com/docs):** Para probar los endpoints técnicos directamente.
## 💻 Cómo desplegar el proyecto localmente

Si deseas correr todo el ecosistema en tu propia máquina a través de contenedores:

**1. Clona el repositorio:**
```bash
git clone [https://github.com/carlo0804/api-churn-clientes.git](https://github.com/carlo0804/api-churn-clientes.git)
cd api-churn-clientes
```

**2. Levanta el Backend (API) con Docker:**
```bash
docker build -t api-churn .
docker run -d -p 8000:8000 --name contenedor-churn api-churn
```
**3. Levanta el Frontend (Streamlit):**
```bash
pip install -r requirements.txt
streamlit run frontend.py
```

## Comunicación API (Ejemplo de Payload)
**1. Petición (POST):**
```bash
{

  "antiguedad_meses": 12,
  "cargo_mensual": 85.5,
  "reclamos_previos": 3,
  "tipo_contrato": "Mes a mes"
}
```

**2. Respuesta de la API (JSON):**
```bash
{
  "alerta_fuga": true,
  "probabilidad_abandono": "72.0%",
  "accion_sugerida": "Ofrecer descuento de retención del 20%"
}