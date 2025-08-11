# Imagine de bază minimalistă
FROM python:3.11-slim

# Setează directorul de lucru în container
WORKDIR /app

# Instalează pachetele de bază (opțional: dacă ai erori la compilare C)
RUN apt-get update && apt-get install -y gcc

# Copiază fișierul de dependențe mai întâi (pentru cache eficient)
COPY requirements.txt .

# Instalează dependențele din requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copiază codul aplicației
COPY . .

# Expune portul aplicației
EXPOSE 8000

# Comanda de rulare a aplicației
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
