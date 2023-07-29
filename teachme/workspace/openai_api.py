import openai

openai.api_key = ''

def generate_text(skill_level, topic):
    prompt = f"The user's skill level is {skill_level}. Please provide a short explainer about the topic {topic}."
    response = openai.Completion.create(engine="gpt-3.5-turbo", prompt=prompt, max_tokens=100)
    return response.choices[0].text.strip()

def grade_answer(question, answer):
    prompt = f"The question is: {question}. The user's answer is: {answer}. Please grade the answer on a scale of 0 to 100."
    response = openai.Completion.create(engine="gpt-3.5-turbo", prompt=prompt, max_tokens=10)
    return int(response.choices[0].text.strip())
