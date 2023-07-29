from flask import Flask
from controllers import LearningController

app = Flask(__name__)
controller = LearningController()

@app.route('/', methods=['GET', 'POST'])
def index():
    return controller.index()

if __name__ == '__main__':
    app.run(debug=True)
