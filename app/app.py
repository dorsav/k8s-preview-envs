from flask import Flask
# test
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Show me what you got!!!'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

