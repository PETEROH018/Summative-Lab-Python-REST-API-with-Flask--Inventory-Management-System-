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

@app.route('/inventory',methods = ['POST'])
def add_item():
    new_item = request.get_json()
    id = max([item["id"] for item in items])+1
    items.append({"id":id,"brands":new_item["brands"],"product_name":new_item["product_name"],"code":new_item["code"]})
    return jsonify({"message":f"{new_item["product_name"]} has been succesfully added to the inventory list"}),201

@app.route('/inventory/<int:id>',methods = ['PUT','PATCH'])
def update_item(id):
    data = request.get_json()
    item_to_update = next((i for i in items if i["id"] == id),None)
    if item_to_update:
        if "product_name" in data and "brands" in data:
            item_to_update["product_name"] = data["product_name"]
            item_to_update["brands"] = data["brands"]
        elif "product_name" in data and "brands" not in data:
            item_to_update["product_name"] = data["product_name"]
        else:
            item_to_update["brands"] = data["brands"]
        return jsonify({"message":f"{item_to_update["product_name"]} has been updated successfully"}),200
    else:
        return jsonify({"error":f"No item with id:{id}"}),404

@app.route('/inventory/<int:id>',methods = ['DELETE'])
def delete_item(id):
    global items
    item_to_delete = next((i for i in items if i["id"] == id),None)
    if item_to_delete:
        items=[item for item in items if item['id']!=id]
        return jsonify({"message":f"{item_to_delete["product_name"]} has been deleted successfully"}),200
    else:
        return jsonify({"error":f"No item with id:{id}"}),404

if __name__ == '__main__':
    app.run(debug=True)
