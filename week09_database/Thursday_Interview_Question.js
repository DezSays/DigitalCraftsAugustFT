// `Hurricane Ian has caused massive power outages across FL and we need to determine how many people are without power. Using the random data API, create a database that holds customers of Florida Power and store their name, phone number, and address. Only people with FL, GA, SC, and NC addresses should be stored. Add to each customer a field that indicates if they have power or not. Write db query that retrieves all users from the db without power. `
// https://random-data-api.com/documentation

// 1). Make API call that gets 1000 random users
// 2). Filter out anyone not in the affected states
// 3). Remove unnecessary fields of info
// 4). Randomly assign if person has power
// 5). Using sequelize, create a db and table for storing customers
// 6). Store those customers in the db
// 7). Write a separate function that only retrieves customers without power from the database 

