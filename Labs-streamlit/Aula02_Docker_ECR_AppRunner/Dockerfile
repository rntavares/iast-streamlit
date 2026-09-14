# Imagem base — leve e oficial do Python
FROM python:3.11-slim

WORKDIR /app

# Copia primeiro só as dependências (aproveita o cache de build do Docker)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante do código
COPY . .

# Porta usada pela aplicação Streamlit
EXPOSE 8501

CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
