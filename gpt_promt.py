from openai import OpenAI
from config import apiKey
client = OpenAI(api_key = apiKey)
OPENAI_API_KEY = apiKey
response = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Hello! How can I use the OpenAI API?"}
  ],
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

# Extract and print the assistant's response
print(response['choices'][0]['message']['content'])
