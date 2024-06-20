FastAPI no Google Colab com Leitura de Planilha JSON
Este projeto demonstra como criar uma API utilizando o FastAPI no Google Colab, que lê dados de uma planilha JSON e fornece endpoints para acessar esses dados. A aplicação utiliza o ngrok para tornar a API acessível publicamente.
Link: https://colab.research.google.com/drive/1OTQaMJGGPDjhQB3Xz_Y5goce1bekHl9B?usp=sharing

Visão Geral
A aplicação FastAPI criada neste projeto tem dois endpoints principais:

GET /: Endpoint que retorna uma mensagem "Hello World".
GET /index: Endpoint que lê dados de uma planilha JSON e retorna esses dados no formato JSON.
Pré-requisitos
Conta no Google Colab.
Pacotes Python: fastapi, uvicorn, nest-asyncio, pyngrok, pandas.
Instalação
Clone este repositório ou copie o código fonte para seu ambiente de desenvolvimento local.

Instale as dependências necessárias:
!pip install fastapi uvicorn[standard] nest-asyncio pyngrok pandas
Configuração e Execução
Criar o arquivo JSON de dados:

No Google Colab, execute o código abaixo para criar um DataFrame de exemplo e salvá-lo como um arquivo JSON:

python
Copiar código
import pandas as pd

data = {
    "id": [1, 2, 3],
    "name": ["John Doe", "Anna Smith", "Peter Jones"],
    "position": ["Software Engineer", "Data Scientist", "Project Manager"]
}

df = pd.DataFrame(data)
df.to_json('data.json', orient='records')
Desenvolver a API FastAPI:

Crie e execute a aplicação FastAPI com o seguinte código:

python
Copiar código
from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import json
from pyngrok import ngrok
import nest_asyncio
import uvicorn

app = FastAPI()
nest_asyncio.apply()

def read_data():
    with open('data.json', 'r') as f:
        data = json.load(f)
    return data

@app.get("/")
def read_root():
    return {"message": "Hello World"}

@app.get("/index")
def get_data():
    data = read_data()
    return data

# Iniciar o túnel ngrok
public_url = ngrok.connect(8000)
print(f"Public URL: {public_url}")

# Iniciar o servidor Uvicorn
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
Acessar os Endpoints:

Hello World: Acesse http://<ngrok-url>/ para verificar a mensagem "Hello World".
Dados JSON: Acesse http://<ngrok-url>/index para visualizar os dados da planilha JSON.
Estrutura do Projeto
plaintext
Copiar código
.
├── data.json
├── README.md
└── app.py
data.json: Arquivo JSON gerado a partir do DataFrame de exemplo.
README.md: Instruções do projeto.
app.py: Código fonte da aplicação FastAPI.
Tecnologias Utilizadas
FastAPI: Framework web moderno e rápido para construir APIs com Python 3.6+ baseado em padrões como Python type hints.
Uvicorn: Servidor ASGI para executar a aplicação FastAPI.
ngrok: Ferramenta para expor localmente servidores web atrás de NATs e firewalls para a internet pública.
Pandas: Biblioteca de manipulação de dados para Python.
Google Colab: Ambiente de desenvolvimento baseado em Jupyter Notebook fornecido pelo Google.
