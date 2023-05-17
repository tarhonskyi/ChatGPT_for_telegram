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
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        stop=None
    )
    # print(response)
    return response.choices[0].text.strip()


def generate_turbo_response(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": f"{prompt}"}],
        max_tokens=2048,
        temperature=0.5,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        stop=None
    )
    # print(response)
    return response.choices[0].message.content.strip()


if __name__ == "__main__":
    while True:
        request = input("You: ")
        if request == "stop":
            break
        text = generate_turbo_response(request)
        print("ChatGPT: ", text)
