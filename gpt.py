import openai
import os

openai.api_key = os.getenv('OPENAI_API_KEY')

completion = openai.ChatCompletion.create(
  model = 'gpt-3.5-turbo',
  messages = [
    {'role': 'user', 'content': 'Hello!'}
  ],
  temperature = 0  
)

print(completion['choices'][0]['message']['content'])
