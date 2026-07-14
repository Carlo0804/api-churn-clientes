from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

app = FastAPI(title="API de Retención de Clientes", description="Predice probabilidad de Churn")

# 1. Cargamos el modelo
modelo = joblib.load('churn_model.pkl')

# 2. Definimos qué datos debe enviar la empresa
class Cliente(BaseModel):
    antiguedad_meses: int
    cargo_mensual: float
    reclamos_previos: int
    tipo_contrato: str

# 3. El Endpoint de predicción
@app.post("/predecir_fuga/")
def predecir(cliente: Cliente):
    # Transformamos el JSON de entrada a un DataFrame
    datos_cliente = pd.DataFrame([cliente.model_dump()])
    
    # Predecimos la clase (0 o 1) y la probabilidad (porcentaje)
    prediccion = modelo.predict(datos_cliente)[0]
    probabilidad = modelo.predict_proba(datos_cliente)[0][1]
    
    # Lógica de negocio para la respuesta
    es_riesgo = bool(prediccion == 1)
    
    return {
        "alerta_fuga": es_riesgo,
        "probabilidad_abandono": f"{round(probabilidad * 100, 1)}%",
        "accion_sugerida": "Ofrecer descuento de retención del 20%" if es_riesgo else "No requiere acción"
    }