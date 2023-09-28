
from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient("mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+1.10.6")

db = client["mydb"]
menu_collection = db["menu"]
order_collection = db["orders"]

# Function to add a new dish to the menu
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

# Route to remove a dish from the menu
@app.route('/remove_dish/<dish_id>',methods=['DELETE','GET'])
def remove_dish(dish_id) : 
    result = menu_collection.delete_one({"dish_id":dish_id})
    if result.deleted_count == 1 :
        return jsonify({"message":"Dish removed from the menu.."}),201
    else :
        return jsonify({"message":"Dish not found in the menu.."}),201


# Route to update dish availability
@app.route('/update_availability/<dish_id>',methods=['PUT'])
def update_availability(dish_id) :
    data = request.json
    available = data.get('available')
    result = menu_collection.update_one(
        {"dish_id":dish_id},
        {"$set":{"available":available}}
    )
    if result.modified_count == 1 :
        return jsonify({"message": f"Availability for dish {dish_id} updated to  {available} ."}), 200
    else :
        return jsonify({"message": "Dish not found in the menu."}), 404



if __name__ == "__main__" :
    app.run(debug=True)