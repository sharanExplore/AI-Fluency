import os
from groq import Groq
from tools import get_weather

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY")
)

question = "Should I carry an umbrella today in Coimbatore?"

print("=== REACT AGENT ===")

print("\nUSER:")
print(question)

# Reasoning step
print("\nTHOUGHT:")
print("I need current weather information before answering.")

# Action
print("\nACTION:")
print("Calling weather tool...")

weather = get_weather()

# Observation
print("\nOBSERVATION:")
print(weather)

# Final reasoning using the tool result
prompt = f"""
You are a weather decision assistant.

User question:
{question}

Current weather information:
{weather}

Use the weather information to answer the user's question.

Give:
1. A concise reasoning summary
2. A final answer

Do not invent weather information that is not present in the tool result.
"""

response = client.chat.completions.create(
    model="openai/gpt-oss-120b",
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ]
)

print("\nFINAL ANSWER:")
print(response.choices[0].message.content)