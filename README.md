# IA para Software Developers — Setup

## Requisitos

- Docker Desktop (gratuito)
- VS Code (gratuito)
- Extensión **Dev Containers** en VS Code (`ms-vscode-remote.remote-containers`)

## Primer arranque

```bash
cd ia-para-devs
code .
```

VS Code preguntará: **"Reopen in Container?"** → Aceptar.

La primera vez tarda 3-5 min (descarga imágenes Docker, dependencias Python y modelo phi3).

## Verificar Funcionamiento

Una vez cargado el entorno en el Dev Container de VS Code, ejecuta la verificación en la terminal integrada:

```bash
python /workspace/hello.py
```

Debería mostrar: `✅ Ollama responde en http://ollama:11434` junto con la versión de Python instalada.

---

## 🔌 Servicios y Puertos Disponibles

El entorno inicia automáticamente los siguientes servicios, cuyos puertos están redirigidos a tu máquina local:

*   **Jupyter Notebook**: [http://localhost:8888](http://localhost:8888) (Entorno de desarrollo Python para prácticas).
*   **Ollama**: [http://localhost:11434](http://localhost:11434) (Servicio local de LLM que ejecuta el modelo `phi3`).
*   **PostgreSQL**: `localhost:5432` (Base de datos relacional y vectorial. Credenciales: usuario `dev`, contraseña `dev`, base de datos `llmdb`).
