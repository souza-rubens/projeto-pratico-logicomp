import google.generativeai as genai
from dotenv import load_dotenv
import os
#Loading environment variables from .env file
load_dotenv()

apiKey = os.getenv("API_KEY")

# Configurar a chave de API (cole aqui a chave que você gerou no AI Studio)
genai.configure(api_key=apiKey)
# Criar um modelo de linguagem
model = genai.GenerativeModel("gemini-2.5-flash")
# Testando com uma pergunta simples
resposta = model.generate_content("Explique o que é um algoritmo em poucas palavras.")
print(resposta.text)