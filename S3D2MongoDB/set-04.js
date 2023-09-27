/*Problem 36:
Write a query to find the ride with the highest and lowest `fare`
*/


/*Problem 37:
Write a query to find the average fare and distance for each driver_id*/



/*Problem 38:
Write a query to find driver_id that have completed more than 5 rides.*/



/*Problem 39:
Assuming there is another collection/table called Drivers with driver_id and name fields, write a query to find the name of the driver with the highest fare.*/



/*Problem 40:
Write a query to find the top 3 drivers who have earned the most from fares. Return the drivers' ids and total earnings.*/



/*Problem 41:
Assuming there's a ride_date field of date type in the Rides table / collection, write a query to find all rides that happened in the last 7 days.*/




/*Problem 42:
Write a query to find all rides where the end_location is not set*/



/*Problem 43:
Write a query to calculate the fare per mile for each ride and return the ride ids and their fare per mile, ordered by fare per mile in descending order.*/



/*Problem 44:
Assuming there's another collection/table Passengers with passenger_id and name fields, write a query to return a list of all rides including the driver's name and passenger's name.*/



/*Problem 45:
Write a query to add a tip field to the Rides table / collection.*/
db.Rides.updateAll({},{$set:{tip:null}})