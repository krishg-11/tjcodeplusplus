from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/lectures')
def lectures():
    return render_template('lectures.html')

if __name__ == '__main__':
    app.run()