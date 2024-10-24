from dotenv import load_dotenv
from openai import OpenAI
import os

load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

client = OpenAI()
client.api_key = os.environ["OPENAI_API_KEY"]

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "user", "content": "Say hi to my friends."}
    ]
)

print(completion.choices[0].message.content)