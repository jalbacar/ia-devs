import requests

url = "http://ollama:11434/api/generate"
payload = {
    "model": "qwen2.5:0.5b",
    "prompt": "Say hello and introduce yourself in one sentence.",
    "stream": False
}

print("Sending request to Ollama...")
try:
    response = requests.post(url, json=payload, timeout=15)
    result = response.json()
    if "response" in result:
        print("\n✅ Response from Ollama:")
        print(result["response"])
    elif "error" in result:
        print("\n❌ Ollama returned an error:")
        print(result["error"])
    else:
        print("\n⚠️ Unexpected response format:")
        print(result)
except Exception as e:
    print("\n❌ Error connecting to Ollama:", e)
