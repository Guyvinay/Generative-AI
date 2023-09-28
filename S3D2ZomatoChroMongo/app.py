
from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient("mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+1.10.6")

db = client["mydb"]
menu_collection = db["menu"]
order_collection = db["orders"]

@app.route('/add_dish',methods=['POST'])
def addNewDish():
    data = request.json
    dish_id = data.get('dish_id')
    name = data.get('name')
    price = float(data.get('price'))
    available = data.get('available', False)
    menu_item = {
        "dish_id": dish_id,
        "name": name,
        "price": price,
        "available": available
    }
    menu_collection.insert_one(menu_item)
    response_data = {
        "message":"Menu Item Successfully Added to Menu Items",
        "menu_item":f"{menu_item}"
    }
    return jsonify(response_data)



if __name__ == "__main__" :
    app.run(debug=True)