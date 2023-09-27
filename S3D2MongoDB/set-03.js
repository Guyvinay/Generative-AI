
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
Create a `Rides` collection with the fields defined above.
*/

/*
Problem 29:
Create a `Rides` collection with the fields defined above.
*/

/*
Problem 30:
Create a `Rides` collection with the fields defined above.
*/

/*
Problem 32:
Create a `Rides` collection with the fields defined above.
*/

/*
Problem 33:
Create a `Rides` collection with the fields defined above.
*/

/*
Problem 34:
Create a `Rides` collection with the fields defined above.
*/

/*
Problem 35:
Create a `Rides` collection with the fields defined above.
*/

/*
Problem 36:
Create a `Rides` collection with the fields defined above.
*/

/*
Problem 37:
Create a `Rides` collection with the fields defined above.
*/

/*
Problem 38:
Create a `Rides` collection with the fields defined above.
*/
