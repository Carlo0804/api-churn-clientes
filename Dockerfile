# Usamos una imagen oficial de Python ligera
FROM python:3.10-slim

# Le decimos a Docker dónde trabajar dentro del contenedor
WORKDIR /app

# Copiamos el archivo de dependencias primero (para aprovechar el caché de Docker)
COPY requirements.txt .

# Instalamos las librerías
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos el resto de los archivos (app.py, churn_model.pkl)
COPY . .

# Exponemos el puerto 8000
EXPOSE 8000

# El comando para encender el motor cuando el contenedor nazca
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]