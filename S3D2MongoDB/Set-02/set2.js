/*Problem 16:
Create a `Restaurants`collection with the fields defined above.
*/
db.createCollection(
    "Restaurants",
    {
        "_id":ObjectId,
        "name":String,
        "cuisine_type": String,
        "location": String,
        "average_rating": Number,
        "delivery_available": Boolean
    }
)

/*Problem 17:
 Insert five rows / documents into the Restaurants table / collection with data of your choice*/
db.Restaurants.insertMany([{name:"Rest1",cuisine_type:"cuisine1",location:"location1",average_rating:7,delivery_available:true},{name:"Rest2",cuisine_type:"cuisine2",location:"location2",average_rating:7,delivery_available:true},{name:"Rest3",cuisine_type:"cuisine3",location:"location3",average_rating:7,delivery_available:true},{name:"Rest4",cuisine_type:"cuisine4",location:"location4",average_rating:7,delivery_available:true},{name:"Rest5",cuisine_type:"cuisine5",location:"location5",average_rating:2,delivery_available:false},{name:"Rest6",cuisine_type:"cuisine6",location:"location6",average_rating:9,delivery_available:true},{name:"Rest7",cuisine_type:"cuisine7",location:"location7",average_rating:4,delivery_available:false},{name:"Rest8",cuisine_type:"cuisine8",location:"location8",average_rating:3,delivery_available:false},{name:"Rest9",cuisine_type:"cuisine9",location:"location9",average_rating:9,delivery_available:true},{name:"Rest10",cuisine_type:"cuisine10",location:"location10",average_rating:7,delivery_available:true},{name:"Rest11",cuisine_type:"cuisine11",location:"location11",average_rating:5,delivery_available:false}
])


/*Problem 18:
Write a query to fetch all restaurants, ordered by average_rating in descending order.*/
db.Restaurants.find().sort({average_rating:-1})


/*Problem 19:
Write a query to fetch all restaurants that offer delivery_available and have an average_rating of more than 4.*/
db.Restaurants.find({
    $and:[
        {delivery_available:true},
        {average_rating:{$gt:4}}
    ]
})

/*Problem 20:
Write a query to fetch all restaurants where the cuisine_type field is not set or is null.*/
db.Restaurants.find({
    $or:[
        {cuisine_type:{$exists:false}},
        {cuisine_type:null}
    ]
})

/*Problem 21:
Write a query to count the number of restaurants
that have delivery_available*/
db.Restaurants.countDocuments({delivery_available:true})

/*Problem 22:
Write a query to fetch all restaurants whose location contains 'New York'.*/
db.Restaurants.find({location:{$regex:/New York/i}})
db.Restaurants.find({location:/location1/i})

/*Problem 23:
Write a query to calculate the average average_rating of all restaurants.
*/
db.Restaurants.aggrefate([
    {
        $group:{
            _id:null,
            average_rating:{$avg:"$average_rating"}
        }
    }
])

/*Problem 24:
Write a query to fetch the top 5 restaurants when ordered by average_rating in descending order.*/
db.Restaurants.find().sort({average_rating:-1}).limit(5)


/*Problem 25:
Write a query to delete the restaurant with id 3.
*/
db.Restaurants.deleteOne({_id:ObjectId("65142cabf6f95c40588d61a2")})