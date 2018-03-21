from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return 'index page'

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('app.html',name=name)

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')