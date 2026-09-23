import os
from groq import Groq

client = Groq(
    api_key=os.environ.get("api_key")
)

question = """
Should I carry an umbrella today in Coimbatore?

Analyze the question carefully before answering.
Consider whether you have enough information to make a reliable
recommendation.

Give:
1. A concise reasoning summary
2. A final answer

Do not use external tools.
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

print("=== CHAIN-OF-THOUGHT ===")
print("Question:")
print(question)

print("\nAnswer:")
print(response.choices[0].message.content)