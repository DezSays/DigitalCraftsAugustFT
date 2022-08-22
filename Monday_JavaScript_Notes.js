// This is a comment in javascript

// JavaScript Types:
    // number,
    // string,
    // boolean,
    // object,
    // array 


// How to print to the screen
console.log('Howdy');
    
// This is how you declare a variable (older style)

var firstName = 'Dezarea';
console.log(firstName);

// This is how you declare a variable (new style -- preferred)

let city = 'Atlanta';
console.log(city);

// JavaScript uses 'number', not 'integer' or 'floats'

// How to find the type of something, in this case a number
console.log(typeof(35));

// Booleans are lower cased in js
isRaining = true; 

// Working with arrays, basic printing to the screen
let scores = [3, 4, 7, 3];
console.log(scores);

// How to get the length of an array in js
console.log(scores.length);

// Set up an object and print everything from it
let player = {
    name: "Ronald Acuna Jr.",
    number: 13,
    position: "Right Field"
};
console.log(player);

// From the object above print just the players name
console.log(player.name);

// JavaScript has a built in Date type
let todaysDate = new Date();
console.log(todaysDate);

// Creating a function in JavaScript
function salutations(name) {
    // console.log('Howdy', name)  // option 1: call the function below the closing bracket this way: salutations('Dezarea')
    // return 'Howdy ' + name  // option 2: call the function below the closing bracket this way: console.log(salutations('Dezarea')) 
};

// How to concatenate strings (add strings together)
fullName = 'Dezarea ' + 'Bryan';
console.log(fullName);

// String interpolation
let month = 'August';
let date = 22;
let year = 2022;
console.log(`Today is ${month} ${date}, ${year}`);

// In JavaScript, this is how you will declare a constant (anything set to constant is non alterable)
const PI = 3.14;

// JavaScript incrementors/decrementors
let count = 0;
count++;     // this increments by 1
count++;     // this increments by 1
count--;     // this decrements by 1
count+=5;     // this increments by 5
console.log(`Count: ${count}`);

// Instead of using keywords (such as 'and' or 'or') are replaced with operators:

// If it is raining and the month is august then we want it to print out we're in the dog days of summer
if(isRaining && month == 'August') {
    console.log(`We're in the dog days of summer`)
};

//If it is sunny or if the year is 2022, print no time like the present
if(!isRaining || year == 2022) {
    console.log(`No time like the present`)
};