from openai_api import generate_text, grade_answer

class LearningModel:
    def __init__(self):
        self.skill_level = 0

    def generate_resources(self, topic):
        text = generate_text(self.skill_level, topic)
        return text

    def grade_answer(self, question, answer):
        grade = grade_answer(question, answer)
        self.skill_level = (self.skill_level + grade) / 2
        return self.skill_level
