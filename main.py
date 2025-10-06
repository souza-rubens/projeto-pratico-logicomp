import os
from dotenv import load_dotenv
#Loading environment variables from .env file
load_dotenv()
#Accessing environment variable API_KEY
api_key = os.getenv("API_KEY")
#Checking if API_KEY was successfully loaded
if api_key:
    print("Chave de API carregada com sucesso:", api_key)
else:
    print("Chave de API não encontrada no arquivo .env.")


