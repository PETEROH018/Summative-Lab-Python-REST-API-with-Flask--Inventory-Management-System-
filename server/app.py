from data import get_items
from flask import Flask,make_response,request

app = Flask(__name__)

@app.route('/')
def show_items():
    items= get_items()
    print(type(items))
    return make_response(items)

if __name__ == '__main__':
    app.run(debug=True)