import os
import json
from dotenv import load_dotenv
from openai import OpenAI
from tools import get_student_data

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Define the tool for the LLM
tools = [
    {
        "type": "function",
        "name": "get_student_data",
        "description": "Get the student's private placement application data.",
        "parameters": {
            "type": "object",
            "properties": {},
            "required": [],
            "additionalProperties": False
        }
    }
]

question = "Which companies require my next action and what should I do?"

input_messages = [
    {
        "role": "user",
        "content": question
    }
]

# First call: let the model decide whether it needs the tool
response = client.responses.create(
    model="gpt-5.6",
    tools=tools,
    input=input_messages
)

# Process tool calls
for item in response.output:

    if item.type == "function_call" and item.name == "get_student_data":

        print("Agent decided to use: get_student_data")

        data = get_student_data()

        input_messages.append(item)

        input_messages.append({
            "type": "function_call_output",
            "call_id": item.call_id,
            "output": json.dumps(data)
        })

# Second call: let the model analyze the tool result
final_response = client.responses.create(
    model="gpt-5.6",
    tools=tools,
    input=input_messages
)

print("\nAgent:")
print(final_response.output_text)