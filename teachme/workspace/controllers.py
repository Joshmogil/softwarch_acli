from flask import request, render_template
from models import LearningModel

class LearningController:
    def __init__(self):
        self.model = LearningModel()

    def index(self):
        if request.method == 'POST':
            topic = request.form['topic']
            resources = self.model.generate_resources(topic)
            return render_template('index.html', resources=resources)
        else:
            return render_template('index.html')
