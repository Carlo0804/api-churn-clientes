import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
import joblib

print("Generando datos de clientes...")
np.random.seed(42)
n_clientes = 5000

# Simulamos datos de una empresa de internet/telefonía
data = {
    'antiguedad_meses': np.random.randint(1, 72, n_clientes),
    'cargo_mensual': np.random.uniform(20.0, 120.0, n_clientes),
    'reclamos_previos': np.random.randint(0, 5, n_clientes),
    'tipo_contrato': np.random.choice(['Mes a mes', 'Un año', 'Dos años'], n_clientes, p=[0.5, 0.3, 0.2]),
    'fuga': np.random.choice([0, 1], n_clientes, p=[0.75, 0.25]) # 25% de fuga normal
}
df = pd.DataFrame(data)

# Hacemos que los datos tengan lógica de negocio:
# Si tienen contrato mes a mes, pagan mucho y tienen reclamos, la fuga sube al 100%
df.loc[(df['tipo_contrato'] == 'Mes a mes') & (df['reclamos_previos'] > 2) & (df['cargo_mensual'] > 80), 'fuga'] = 1

X = df.drop('fuga', axis=1)
y = df['fuga']

print("Construyendo el Pipeline...")
# Pipeline de preprocesamiento (Codifica texto y escala números)
preprocesador = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), ['antiguedad_meses', 'cargo_mensual', 'reclamos_previos']),
        ('cat', OneHotEncoder(handle_unknown='ignore'), ['tipo_contrato'])
    ])

# Unimos el preprocesador con el modelo Random Forest
modelo_completo = Pipeline(steps=[
    ('preprocesador', preprocesador),
    ('clasificador', RandomForestClassifier(n_estimators=100, random_state=42))
])

print("Entrenando el modelo...")
modelo_completo.fit(X, y)

# Guardamos el modelo
joblib.dump(modelo_completo, 'churn_model.pkl')
print("¡Modelo entrenado y guardado exitosamente como 'churn_model.pkl'!")