"""Primer script del curso — verifica que el contenedor funciona."""
import requests

try:
    r = requests.get("http://ollama:11434/api/tags", timeout=5)
    print(f"✅ Ollama responde en http://ollama:11434")
    print(f"   Modelos disponibles: {r.json()}")
except Exception as e:
    print(f"❌ No se pudo conectar con Ollama: {e}")
    print("   ¿Está arrancado todo el stack?")

print(f"\n🐍 Python {__import__('sys').version}")
print("📁 /workspace montado correctamente")