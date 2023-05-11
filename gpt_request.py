import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.environ["OPENAI_API_KEY"]


def generate_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=2048,
        temperature=0.5,
    )

    return response.choices[0].text.strip()


if __name__ == "__main__":
    while True:
        print("Введіть запит:")
        request = input(">> ")
        text = generate_response(request)
        print(text)
