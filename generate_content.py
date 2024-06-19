import openai

openai.api_key = 'xxxxxxxxxxxx'

def generate_content(topic):
    response = openai.Completion.create(
        model="text-davinci-004",
        prompt=f"Generate a detailed blog post on the topic: {topic} in academic writing style.",
        max_tokens=1500
    )
    return response.choices[0].text

topic = "Recent advancements in veterinary diagnostics"
content = generate_content(topic)

with open('new_post.html', 'w') as file:
    file.write(f"<h1>{topic}</h1>\n{content}")
