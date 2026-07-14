# API de Predicción de Fuga de Clientes (Customer Churn)

## 📌 El Problema de Negocio
En la industria de telecomunicaciones, el costo de adquirir un cliente nuevo es mucho mayor que el de retener uno existente. Este proyecto es un microservicio de Machine Learning diseñado para identificar clientes con alto riesgo de abandono (Churn) utilizando datos históricos de comportamiento y facturación.

## 🛠️ Stack Tecnológico
* **Data Science & ML:** Python, Pandas, Scikit-Learn (Random Forest).
* **Despliegue (Deployment):** FastAPI, Uvicorn, Joblib.
* **Entorno:** Linux (Ubuntu).

## 🧠 Arquitectura del Modelo
Se entrenó un pipeline completo que incluye:
1. **Preprocesamiento:** `StandardScaler` para variables numéricas (antigüedad, cargos, reclamos) y `OneHotEncoder` para variables categóricas (tipo de contrato).
2. **Clasificación:** `RandomForestClassifier` para capturar relaciones no lineales entre los reclamos y el tipo de contrato.

## 🚀 Cómo probar la API localmente

1. Clona este repositorio.
2. Instala las dependencias: `pip install -r requirements.txt`
3. Ejecuta el servidor: `uvicorn app:app --reload`
4. Accede a la documentación interactiva (Swagger UI) en: `http://127.0.0.1:8000/docs`

## 📊 Ejemplo de Respuesta (Payload)
Al enviar un cliente con contrato "Mes a mes" y múltiples reclamos, la API responde con la probabilidad de abandono y una regla de negocio accionable:

```json
{
  "alerta_fuga": true,
  "probabilidad_abandono": "63.0%",
  "accion_sugerida": "Ofrecer descuento de retención del 20%"
}