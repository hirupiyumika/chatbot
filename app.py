from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = (os.getenv("OPENAI_API_KEY"))

client = OpenAI()

while True:
    question = input("User: ")
    if question != "bye":

        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            max_tokens=50,
            n=1,
            temperature=0,
            messages=[
                {"role": "user", "content": question},
            ],
        )

        for response in response.choices:
            print(f"AI: {response.message.content}")
    else:
        print("AI: Goodbye!")
        break
