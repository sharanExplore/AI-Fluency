import os
from groq import Groq

client = Groq(
    api_key=os.environ.get("api_key")
)

question = """
Should I carry an umbrella today in Coimbatore?

Answer based only on your existing knowledge.
Do not use any external tools.
Give a short answer and explain why.
"""

response = client.chat.completions.create(
    model="openai/gpt-oss-120b",
    messages=[
        {
            "role": "user",
            "content": question
        }
    ]
)

print("=== DIRECT PROMPTING ===")
print("Question:")
print(question)

print("\nAnswer:")
print(response.choices[0].message.content)