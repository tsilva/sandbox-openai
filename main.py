from dotenv import load_dotenv
load_dotenv()

from openai import OpenAI

client = OpenAI()

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Say this is a test",
        }
    ],
    model="gpt-4o",
)
print(chat_completion)