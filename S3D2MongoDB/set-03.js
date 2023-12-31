
/*
Problem 26:
Create a `Rides` collection with the fields defined above.
*/

db.createCollection(
    "Rides",
    {
        "_id":ObjectId(),
        "driver_id": ObjectId(),
        "passenger_id": ObjectId(),
        "start_location": String,
        "end_location": String,
        "distance": Number,
        "ride_time": Number,
        "fare": Number
    }
)

/*
Problem 27:
 Insert five rows / documents into the Rides table / collection with data of your choice.*/


db.Rides.insertMany([{start_location:"Start3",end_location:"End3",distance:123,ride_time:13,fare:12113},{start_location:"Start4",end_location:"End4",distance:124,ride_time:14,fare:12114},{start_location:"Start5",end_location:"End5",distance:125,ride_time:15,fare:12115},{start_location:"Start6",end_location:"End6",distance:126,ride_time:16,fare:12116},{start_location:"Start7",end_location:"End7",distance:127,ride_time:17,fare:12117}
])


/*
Problem 28:
 Write a query to fetch all rides, ordered by fare in descending order.*/

db.Rides.find().sort({fare:-1})


 /*
Problem 29:
Write a query to calculate the total distance and total fare for all rides.*/

db.Rides.aggregate({
    $group:{
        _id:null,
        distance:{$sum:"$distance"},
        fare:{$sum:"$fare"}
    }
})

/*
Problem 30:
Create a `Rides`Write a query to calculate the average ride_time of all rides. collection with the fields defined above.
*/

db.Rides.aggregate({
    $group:{
        _id:null,
        avg_ride_time:{
            $avg:"$ride_time"
        }
    }
})

/*
Problem 31:
Write a query to fetch all rides whose start_location or end_location contains 'Downtown'.*/

db.Rides.find({
    $or:[
        {start_location:/Start1/i},
        {end_location:/End2/i}
    ]
})
db.Rides.find({
    $or:[
        {start_location: {$regex:/Start1/i} },
        {end_location:{$regex:/End2/i} }
    ]
})
/*
Problem 32:
Write a query to count the number of rides for a given driver_id.*/

const driver_id = ObjectId("4");
db.Rides.countDocuments({driver_id:driver_id})

/*
Problem 33:
Write a query to update the fare of the ride with id 4.*/


db.Rides.updateOne(
    {_id:ObjectId("651455aff6f95c40588d61ac")},
    {$set:{fare:1717171}}
)


/*
Problem 34:
Write a query to calculate the total fare for each driver_id.*/

db.Rides.aggregate([
    {
      $group: {
        _id: "$driver_id",
        totalFare: { $sum: "$fare" }
      }
    }
  ])
  

/*
Problem 35:
Write a query to delete the ride with id 2.*/

db.Rides.deleteOne({_id:ObjectId("")})
