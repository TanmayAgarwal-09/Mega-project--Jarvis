from openai import OpenAI
client=OpenAI(api_key="sk-proj-5H5QQuTR6UIDoR3O3RFFT3BlbkFJ2kI31htaN5cYzn6W4fOP")
completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a virtual assistant name jarvis, skilled in general tasks like alexa and google cloud."},
    {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
  ]
)

print(completion.choices[0].message.content)
