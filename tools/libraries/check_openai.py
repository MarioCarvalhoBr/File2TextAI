import os
import yaml
import time
import base64
import re
from openai import OpenAI

# Carregar a configuração do arquivo config.yaml
with open('config.yaml', 'r') as config_file:
    config = yaml.safe_load(config_file)
    
os.environ['OPENAI_API_KEY'] = config['OPENAI_API_KEY']

client = OpenAI()

# Função para explicar uma tabela
def explain_text(question_text):
    model = "gpt-4o-mini"
    prompt_system = "Seu nome é Thales e você é especialista em perguntas sobre física."
    user_question = f"Explique pergunta:\n\n{question_text}"

    # Requisição ao modelo
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": prompt_system},
            {"role": "user", "content": user_question}
        ],
        frequency_penalty=1,
        presence_penalty=1,
        temperature=0.3,
    )
    return response.choices[0].message.content


def explain_image_base64(image_base64, is_save=False):
    
    # Getting the base64 string
    base64_image = image_base64

    # Salvar o arquivo base64_image.txt
    with open('base64_image.txt', 'w') as f:
        f.write(base64_image)

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        frequency_penalty=1,
        presence_penalty=1,
        temperature=0.3,
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "Descreva em detalhes a imagem como se você fosse um especialista no assunto.",
                    },
                    {
                        "type": "image_url",
                        "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"},
                    },
                ],
            }
        ],
    )

    message = (response.choices[0].message.content)

    if is_save:
        with open('resposta.txt', 'w') as f:
            f.write(message)

    return message


# Exemplo de uso
if __name__ == "__main__":
    question_text = """
    O que é a força de atrito? Dê um exemplo. 
    """
    explanation = explain_text(question_text)
    print("Explicação:")
    print(explanation)

    # Exemplo de uso para explicar uma imagem
    image_base64 = base64.b64encode(open("image.png", "rb").read()).decode("utf-8")
    explanation = explain_image_base64(image_base64, is_save=True)
    print("\n\nExplicação da imagem:")
    print(explanation)