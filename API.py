from dotenv import load_dotenv
from flask import Flask, request, jsonify
from openai import OpenAI
import os

load_dotenv()
API_SECRET = "minha_chave_super_secreta"
app = Flask(__name__)
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@app.route("/perguntar", methods=["POST"])
def perguntar():
    
    chave = request.headers.get("x-api-key")

    if chave != API_SECRET:
        return jsonify({"erro": "Acesso negado"}), 403
    
    
    dados = request.get_json()
    pergunta = dados.get("texto")

    resposta = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "Responda sempre em português do Brasil"},
        {"role": "user", "content": pergunta}
    ]
)

    return jsonify({"resposta": resposta.choices[0].message.content})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)