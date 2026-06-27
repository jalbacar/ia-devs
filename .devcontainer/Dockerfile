FROM python:3.12-slim

# Instalar dependencias del sistema necesarias
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    build-essential \
    git \
    && rm -rf /var/lib/apt/lists/*

# Actualizar pip
RUN pip install --no-cache-dir --upgrade pip

# Instalar dependencias de Python necesarias para el curso
RUN pip install --no-cache-dir \
    langchain \
    langchain-community \
    langchain-openai \
    openai \
    chromadb \
    jupyter \
    requests \
    pytest \
    black \
    python-dotenv \
    pandas \
    fastapi \
    uvicorn \
    sqlalchemy \
    pydantic \
    hypothesis
