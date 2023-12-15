import os
from dotenv import load_dotenv

from mistralai.client import MistralClient
from mistralai.models.chat_completion import ChatMessage

load_dotenv(override=True)
api_key = os.getenv("MISTRAL_API_KEY")
model = "mistral-tiny"

client = MistralClient(api_key=api_key)

messages = [
    ChatMessage(role="user", content="What is the capital of France?"),
]

# No Streaming
chat_response = client.chat(
    model=model,
    messages=messages,
)
print(chat_response.choices[0].message.content)

# With Streaming
for chunk in client.chat_stream(model=model, messages=messages):
    print(chunk.choices[0].delta.content, end=" ")
