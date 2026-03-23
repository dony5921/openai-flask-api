#  OpenAI Flask API - Integração via Terminal

API REST desenvolvida em Python com Flask para integração com a API da OpenAI, permitindo realizar perguntas diretamente pelo terminal do VSCode.

##  Contexto do projeto

Este projeto foi criado para contornar limitações de ambiente corporativo, onde o uso direto do ChatGPT não é permitido.

A solução permite consumir a API da OpenAI localmente, possibilitando consultas e geração de respostas via terminal.

## ⚙️ Funcionalidades

*  Integração com API Key da OpenAI
*  Envio de perguntas via terminal
*  Retorno de respostas geradas por IA
*  Endpoint REST para integração com outras aplicações

##  Tecnologias

* Python
* Flask
* OpenAI API

## ▶️ Como executar

```bash
git clone https://github.com/SEU_USERNAME/openai-flask-api.git
cd openai-flask-api
pip install -r requirements.txt
python API.py
```

##  Configuração

Configure sua chave da OpenAI como variável de ambiente:

```bash
OPENAI_API_KEY=sua_chave_aqui
```

##  Endpoint

### POST /perguntar

#### Request

```json
{
  "texto": "Como criar um robô padrão RPA?"
}
```

#### Response (exemplo)

```json
{
  "resposta": "Texto gerado pela OpenAI com base na pergunta enviada."
}
```

## 💻 Uso via terminal

Após iniciar a API, você pode enviar perguntas e receber respostas diretamente no terminal.

## 📌 Objetivo

Demonstrar integração com APIs externas (OpenAI), construção de APIs REST com Flask e criação de soluções práticas para restrições de ambiente corporativo.

## 👨‍💻 Autor

Adonizedeque Gonçalves dos Santos.
