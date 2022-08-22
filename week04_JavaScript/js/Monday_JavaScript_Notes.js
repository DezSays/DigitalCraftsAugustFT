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

// Loose comparison(evaluates the value): == vs. Strict Comparison(evaluates value AND type) ===

// Even though there are no floats, we can still get decimals. To divide you could:
console.log(5/2);

// Conditional statement:
if(!isRaining) {
    console.log('You can go outside');
}
else if(isRaining){
        console.log('You need to stay inside');
};

// Switch statements generually are used when we have to check several conditions. This keeps us from writing too many else if statements. 
let day = new Date().getDay();    //this will give you a number representing the day of the week (sun:0, mon:1, etc.)

switch (day) {
    case 0:
        console.log(`No chick fil a for you`)
        break
    case 1:
        console.log(`Mondays...`)
        break
    case 2:
        console.log(`T-Mobile Tuesday`)
        break
    case 3:
        console.log(`Hump day!`)
        break
    case 4:
        console.log(`Almost the weekend!`)
        break
    case 5:
        console.log(`Friday!`)
        break
    case 6:
        console.log(`Slick Deals Saturday`)
        break
    default: 
        console.log(`Enter a valid day of the week`)
}


// How to do loops in JavaScript

let days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

// Example of a for loop
for(let index = 0; index < days.length; index++){
    console.log(days[index])
}

// Example of a while loop
let i = 0;
while(i < days.length) {
    console.log(days[i]);
    i++;
}


// Iterate backwards in an array
for (let i = days.length - 1; i >= 0; i--) {
    console.log(days[i]);
}

//Print out every day of the week that falls on an odd index
for(let i = 1; i < days.length; i+=2) {
    console.log(days[i]);
};

//Print out every day of the week that falls on an even index
for(let i = 0; i < days.length; i+=2) {
    console.log(days[i]);
};