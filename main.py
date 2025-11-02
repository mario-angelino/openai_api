import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)

prompt = """
    Você é um especialista tradutor de textos de português oara Inglês.
    Apenas traduza e responda a tradução do texto que você receber.
"""

# Receber a resposta toda de uma vez
response = client.chat.completions.create(
    model='gpt-5-nano-2025-08-07',
    messages=[
        {
            "role": "system",
            "content": prompt
        },
        {
            "role": "user",
            "content": "O livro está na mesa"
        }
    ],
)
print(response.choices[0].message.content)

# Receber a resposta em streaming
"""
stream = client.chat.completions.create(
    model = 'gpt-5-nano-2025-08-07',
    messages=[
        {"role": "user", "content": "Me fale mais sobre o Fiat Elba 1988"}
    ],
    stream=True
)

for chunk in stream:
    if chunk.choices[0].delta.content is not None:
        print(chunk.choices[0].delta.content, end='')
"""


# response = client.responses.create(
#    model="gpt-4o",
#    input="Testando variável de ambiente!",
# )
# print(response.output_text)
