// **Problem 1:**
// - **Prerequisite**: Understand creating tables in SQL / collections in MongoDB
// - **Problem**: Create a **`Customers`** table / collection with the following fields: **`id`** (unique identifier), **`name`**, **`email`**, **`address`**, and **`phone_number`**.
// ->

db.createCollection(
"Customers", 
{
    "_id":ObjectId,
    "name":String,
    "email":String,
    "address":String,
    "phone_number":String
}
)

/*
**Problem 2:**

- **Prerequisite**: Understand inserting data into SQL tables / MongoDB collections
- **Problem**: Insert five rows / documents into the **`Customers`** table / collection with data of your choice.
*/
db.Customers.insertMany([{ name: "cus5", email: "cus5@gmail.com", address: "add5", phone: "9825738156" },{ name: "cus6", email: "cus6@gmail.com", address: "add6", phone: "9825738157" },{ name: "cus7", email: "cus7@gmail.com", address: "add7", phone: "9825738158" },{ name: "cus8", email: "cus8@gmail.com", address: "add8", phone: "9825738159" },{ name: "cus9", email: "cus9@gmail.com", address: "add9", phone: "98257381510" },{ name: "cus10", email: "cus10@gmail.com", address: "add10", phone: "98257381511" },{ name: "cus11", email: "cus11@gmail.com", address: "add11", phone: "9825738153" },{ name: "cus12", email: "cus12@gmail.com", address: "add12", phone: "98257381512" }])

/*
**Problem 3:**

- **Prerequisite**: Understand basic data fetching in SQL / MongoDB
- **Problem**: Write a query to fetch all data from the **`Customers`** table / collection.

*/

db.Customers.find({})

/*
**Problem 4:**

- **Prerequisite**: Understand how to select specific fields in SQL / MongoDB
- **Problem**: Write a query to select only the **`name`** and **`email`** fields for all customers.
*/
db.Customers.find({},{name:1,email:1})
db.customers.find({}, { _id: 0, name: 1, email: 1 })
/*

{} is the filter criteria, which selects all documents in the collection.
The second parameter specifies the projection, where _id: 0 means to exclude the _id field, and name: 1 and email: 1 mean to include the name and email fields.
*/

/*
**Problem 5:**
Problem: Write a query to fetch the customer with the id of 3.
*/

db.Customers.find({_id:3})
// d.Customers.find({},{name:"Vinay"})
d.Customers.find({name:"Vinay"})

/*var ObjectId = require('mongodb').ObjectId;
var customerId = ObjectId("3");
db.customers.find({ _id: customerId })*/

/*
**Problem 6:**
 Write a query to fetch all customers whose name starts with 'A'.
*/

db.customers.find({ name: /^A/ })

/*
**Problem 7:**
Write a query to fetch all customers, ordered by name in descending order.
*/
//Desc
db.customers.find().sort({ name: -1 })
//ASC
db.customers.find().sort({ name: 1 })



/*
**Problem 8:**
Write a query to update the address of the customer with id 4.
*/
db.Customers.updateOne(
  {name:"Zoe"},
 {$set:{
 address:"New York"}
 }
)



/*
**Problem 9:**
Write a query to fetch the top 3 customers when ordered by id in ascending order.
*/
db.Customers.find().sort({_id:-1}).limit(3)
db.Customers.find().sort({name:1}).limit(3)
db.Customers.find().limit(3)

/*
**Problem 10:**
// Write a query to delete the customer with id 2.
*/
db.Customers.deleteOne({_id:ObjectId("65139357f6f95c40588d6195")})

/*
**Problem 11:**
Write a query to count the number of customers.
*/
db.Customers.countDocuments()

/*
**Problem 12:**
Write a query to fetch all customers except the first two when ordered by id in ascending order.
*/
db.Customers.find().sort({_id:1}).skip(2);
db.Customers.find().sort({_id:-1}).skip(2)

/*
**Problem 13:**
Write a query to fetch all customers whose id is greater than 2 and name starts with 'B'.*/
db.Customers.find({
    $and:[
        {_id: {$gt: ObjectId("65139357f6f95c40588d6192")}},
        {name:/^c/}
    ]
})