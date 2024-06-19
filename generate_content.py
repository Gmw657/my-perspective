import openai
import os

openai.api_key = os.getenv('OPENAI_API_KEY')

def generate_content(topic):
    prompt = (
        f"Write a detailed examination of the power struggle between the TPLF and PP, "
        f"contextualized within Ethiopia's shift towards a new political order post-Oromo protests. "
        f"Discuss the geopolitical influences of Eritrea and the Amhara region, focusing on territorial disputes, "
        f"historical grievances, and their impact on Tigray. "
        f"Provide a thorough analysis in an academic writing style."
    )
    response = openai.Completion.create(
        model="text-davinci-004",
        prompt=prompt,
        max_tokens=1500
    )
    return response.choices[0].text

topic = "Power and Paradox: The Struggle for Dominance in a New Ethiopia"
content = generate_content(topic)

with open('new_post.html', 'w') as file:
    file.write(f"<h1>{topic}</h1>\n{content}")
