import os
from groq import Groq

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY")
)

question = """
A student has an exam tomorrow.

They have 3 hours available tonight.
They need to study DSA, SQL, and aptitude.

What should they study first and why?
Give a concise reasoning summary and a final recommendation.
"""

print("=== SELF-CONSISTENCY EXPERIMENT ===")
print("\nQuestion:")
print(question)

for i in range(5):

    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {
                "role": "user",
                "content": question
            }
        ],
        temperature=0.7
    )

    answer = response.choices[0].message.content

    print(f"\n--- RUN {i + 1} ---")
    print(answer)