import streamlit as st
import requests

st.set_page_config(page_title="Chat de IA — Prácticas", page_icon="🤖", layout="centered")

st.title("🤖 Chat con Ollama Local")
st.write("Interactúa con los modelos de lenguaje locales de forma visual para tus ejercicios de prompting.")

# Inicializar historial de chat
if "messages" not in st.session_state:
    st.session_state.messages = []

# Obtener lista de modelos disponibles en Ollama
try:
    r = requests.get("http://ollama:11434/api/tags", timeout=3)
    models = [m["name"] for m in r.json().get("models", [])]
except Exception:
    models = ["qwen2.5:0.5b"]

if not models:
    models = ["qwen2.5:0.5b"]

# Selector de modelo
model_selected = st.selectbox("Selecciona el modelo de IA:", models, index=0)

# Mostrar historial de chat
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Entrada del usuario
if prompt := st.chat_input("Escribe tu prompt aquí..."):
    # Añadir mensaje al historial
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generar respuesta
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        message_placeholder.markdown("Pensando...")
        try:
            r = requests.post(
                "http://ollama:11434/api/generate",
                json={"model": model_selected, "prompt": prompt, "stream": False},
                timeout=30
            )
            response_text = r.json().get("response", "No se encontró respuesta.")
        except Exception as e:
            response_text = f"❌ Error al conectar con Ollama: {e}"
        
        message_placeholder.markdown(response_text)
        st.session_state.messages.append({"role": "assistant", "content": response_text})
