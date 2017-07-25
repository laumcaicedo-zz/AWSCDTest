from flask import Flask, request

app = Flask(__name__)
app = Flask(__name__)

class HelloWorld(Resource):
    def get(self):
        text = "Hello World!"
        return text


if __name__ == '__main__':
    # Runn Flask
    app.run(debug=True, host='0.0.0.0', port=int("5000"))
# pass
