import openai
import os

def generate_content(topic):
    prompt = (
        f"Write a detailed examination of the power struggle between the TPLF and PP, "
        f"contextualized within Ethiopia's shift towards a new political order post-Oromo protests. "
        f"Discuss the geopolitical influences of Eritrea and the Amhara region, focusing on territorial disputes, "
        f"historical grievances, and their impact on Tigray. "
        f"Provide a thorough analysis in an academic writing style."
    )
    print(f"Prompt: {prompt}")
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt},
        ]
    )
    print(f"Response: {response}")
    return response.choices[0].message['content']

if __name__ == "__main__":
    openai.api_key = os.getenv('OPENAI_API_KEY')
    if not openai.api_key:
        raise ValueError("OpenAI API key is not set")
    else:
        print(f"OpenAI API Key: {openai.api_key}")

    topic = "Power and Paradox: The Struggle for Dominance in a New Ethiopia"
    try:
        content = generate_content(topic)
        with open('new_post.html', 'w') as file:
            file.write(f"<h1>{topic}</h1>\n{content}")
        print("Content generation successful")
    except Exception as e:
        print(f"Error: {e}")
