# TP COMPOSE — image de l'API (Python + Flask)
FROM python:3.12-alpine

WORKDIR /app

# On installe d'abord les dépendances : cette étape est mise en cache par Docker
# et ne sera pas rejouée si seul le code Python change.
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Puis le code de l'API.
COPY app.py .

EXPOSE 5000

CMD ["python", "app.py"]
