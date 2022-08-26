

// This is a basic function
function area(length, width) {
    return length * width;
};
let areaResult = area(5,5)
console.log(areaResult)


// Arrow function
let circumference = (radius) => {
    const PI = 3.14;
    return PI * (radius^2);
};
let circResult = circumference(10)
console.log(circResult)


// Anonymous Function
const sum = function(number1, number2) {
    return number1 + number2;
};
let sumResult = sum(5,5)
console.log(sumResult)



