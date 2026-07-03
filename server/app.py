from data import get_items
from flask import Flask,make_response,request,jsonify

app = Flask(__name__)
items = get_items()

@app.route('/inventory',methods = ["GET"])
def show_items():
    return make_response(items),200

@app.route('/inventory/<int:id>',methods = ["GET"])
def show_item(id):
    item = next((i for i in items if i["id"] == id),None)
    if item:
        return make_response(item),200
    else:
        return jsonify({"error":f"No item with id:{id}"}),404

if __name__ == '__main__':
    app.run(debug=True)