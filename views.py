from flask import Flask, render_template

loise= Flask(__name__)

@loise.route('/')#localhost5000/
def index():
    return render_template('index.html')

if __name__ == '__main__':
    loise.run(debug= True)