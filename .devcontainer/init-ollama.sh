#!/bin/bash
# Script para inicializar modelos en Ollama de forma segura

echo "🤖 Esperando a que el servicio Ollama esté listo..."
OLLAMA_HOST="ollama"
OLLAMA_PORT="11434"
MAX_ATTEMPTS=30
ATTEMPT=1

# Bucle para esperar a que Ollama responda
while [ $ATTEMPT -le $MAX_ATTEMPTS ]; do
  if curl -s "http://$OLLAMA_HOST:$OLLAMA_PORT/api/tags" > /dev/null; then
    echo "✅ Servicio Ollama detectado en http://$OLLAMA_HOST:$OLLAMA_PORT"
    break
  fi
  echo "⏳ Intento $ATTEMPT/$MAX_ATTEMPTS: Ollama no responde aún. Esperando 2 segundos..."
  sleep 2
  ATTEMPT=$((ATTEMPT + 1))
done

if [ $ATTEMPT -gt $MAX_ATTEMPTS ]; then
  echo "⚠️ Advertencia: No se pudo conectar con el servicio Ollama tras $MAX_ATTEMPTS intentos."
  echo "Puedes intentar descargar el modelo manualmente más tarde con: ollama pull phi3"
  exit 0
fi

# Intentar descargar el modelo phi3 (y smollm:135m si se usa)
echo "📥 Descargando modelo phi3..."
if curl -s -X POST "http://$OLLAMA_HOST:$OLLAMA_PORT/api/pull" -d '{"name": "phi3"}' > /dev/null; then
  echo "✅ Modelo phi3 descargado correctamente."
else
  echo "⚠️ Advertencia: Falló la descarga del modelo phi3."
fi

echo "📥 Descargando modelo smollm:135m..."
if curl -s -X POST "http://$OLLAMA_HOST:$OLLAMA_PORT/api/pull" -d '{"name": "smollm:135m"}' > /dev/null; then
  echo "✅ Modelo smollm:135m descargado correctamente."
else
  echo "⚠️ Advertencia: Falló la descarga del modelo smollm:135m."
fi

exit 0
