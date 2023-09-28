
from flask import Flask, request, jsonify
from pymongo import MongoClient
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "http://127.0.0.1:5000/view_orders"}})  
client = MongoClient("mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+1.10.6")

db = client["mydb"]
menu_collection = db["menu"]
order_collection = db["orders"]

# Function to add a new dish to the menu
@app.route('/add_dish',methods=['POST'])
@cross_origin(origin='http://127.0.0.1:5000', headers=['Content-Type', 'Authorization'])
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

#Route to take new order
@app.route('/place_order',methods=['POST'])
def place_order() :
    data = request.json
    customer_name = data.get("customer_name")
    order_items = data.get("order_items")
    total_price = sum(item['price']
                      for item in menu_collection
                      .find({"dish_id":{
                                  "$in":order_items}}))
    order = {
        "customer_name":customer_name,
        "order_items":order_items,
        'status': 'received',
        "total_price":total_price
    }
    result = order_collection.insert_one(order)
    return jsonify({"message":f"Order recieved! OrderId: {result.inserted_id}"}),201

#Route to update order status
@app.route('/update_order_status/<order_id>',methods=['PUT'])
def update_order_status(order_id) :
    data = request.json
    new_status = data.get("status")
    # result = order_collection.update_one(
    #     {"_id":f"ObjectId({order_id})"},
    #     {"$set":{"status":new_status}}
    #     )
    result = order_collection.update_one({"_id": order_id}, {"$set": {"status": new_status}})
    print(order_id)
    if result.modified_count == 1 :
        return jsonify({"message": f"Order {order_id} status updated to {new_status}."}), 200
    else :
        return jsonify({"message": "Order not found."}), 404


#Route to view all orders
@app.route('/view_orders',methods=['GET'])
@cross_origin(origin='http://127.0.0.1:5000', headers=['Content-Type', 'Authorization'])
def view_orders() :
    orders = list(order_collection.find())
    displayed_orders = [] 
    for order in orders :
        order_item = {
            "order_id":str(order["_id"]),
            "customer_name":order["customer_name"],
            "status":order["status"],
            "order_items":[
                {
                    "name":item["name"],
                    "price":item["price"]
                }
                for item in menu_collection.find({"dish_id":{"$in":order["order_items"]}})
            ],
            "total_price":order["total_price"]
        }
        displayed_orders.append(order_item)
    return jsonify(displayed_orders),200


if __name__ == "__main__" :
    app.run(debug=True)