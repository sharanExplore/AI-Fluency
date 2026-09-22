import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

student_data = """
TechCorp - Software Engineer - Applied - Test completed - Interview pending
DataSoft - Backend Developer - Interview completed
CloudWorks - Full Stack Developer - Applied - Test not completed
FinTech Labs - Software Engineer - Offer received
"""

question = """
Which companies require my next action and what should I do?
"""

response = client.responses.create(
    model="gpt-5.6",
    input=f"""
You are a placement assistant.

Here is the student's placement information:

{student_data}

Answer this question:
{question}

Give a short and clear answer.
"""
)

print("\nAssistant:")
print(response.output_text)
