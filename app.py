from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hallo Kurs 25-01!'

if __name__ == '__main__':
    app.run(debug=True)
