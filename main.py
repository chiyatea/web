from flask import Flask
app = Flask(__name__)
@app.route('/')
def index():
    return 'Hello, World!'

@app.route('/about_me')
def about_me():
    return 'hellooooooooooooo'

if __name__ == '__main__':
    app.run(debug=True)