import requests

url = "http://127.0.0.1:5000/perguntar"

pergunta = input("Digite sua pergunta: ")

response = requests.post(url, json={"texto": pergunta},
headers={"x-api-key": "minha_chave_super_secreta"}
)

if response.status_code == 200:
    print("Resposta da IA:\n")
    print(response.json()["resposta"])
else:
    print("Erro:", response.text)