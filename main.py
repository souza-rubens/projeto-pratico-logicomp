import os
from dotenv import load_dotenv
import google.generativeai as genai
import random

#Loading environment variables from .env file
load_dotenv()
#Accessing environment variable API_KEY
api_key = os.getenv("API_KEY")
#Checking if API_KEY was successfully loaded
if api_key:
    print("Chave de API carregada com sucesso:")
else:
    print("Chave de API não encontrada no arquivo .env.")

genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-2.5-flash")

puzzles_dir = "puzzles"

# Listar arquivos .txt dentro da pasta
arquivos = [f for f in os.listdir(puzzles_dir) if f.endswith(".txt")]

if not arquivos:
    raise FileNotFoundError("Nenhum arquivo .txt encontrado na pasta 'puzzles'.")

# Choose a random puzzle
arquivo_escolhido = random.choice(arquivos)
caminho_puzzle = os.path.join(puzzles_dir, arquivo_escolhido)

# Read the puzzle content 
with open(caminho_puzzle, "r", encoding="utf-8") as f:
    puzzle = f.read().strip()

# Strategy for not asking too many questions
puzzle += ". Traduza o problema para o Z3."

# Z3 with correct answer
# ----- PROGRESS -------

resposta = model.generate_content(puzzle)

print(resposta.text)
