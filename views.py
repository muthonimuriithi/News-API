from flask import Flask, render_template

loise= Flask(__name__)

@loise.route('/')#localhost5000/
def index():
    message = 'Hello World, I am pleased'
    return render_template('index.html', message= message)

if __name__ == '__main__':
    loise.run()