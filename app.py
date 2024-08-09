from flask import Flask

app = Flask(__name__)

@app.route('/')
def welcome() :
    return "welcome to Flask"

print(__name__)

if __name__ == '__main__' :
    app.run()