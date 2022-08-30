const displayTemp = document.getElementById('tempNum');
const heatIndex = document.getElementById('heatNum')

currentWeather = {
    temp: 0,
    heatIndex: 0
}

const getWeather = () => {
    // Query parameters by a ?
    fetch('http://api.openweathermap.org/data/2.5/weather?q=Atlanta&appid=b68f35e8bcd7df3748b5e67d1b67462d&units=imperial')
    // Response is stored in the response variable
    .then(response => {
        // response.json() converts the response to json, which we can easily manipulate
        return response.json();
    })
    .then(data => {
        console.log(data)
        displayTemp.innerText = Math.round(data.main.temp)
        heatIndex.innerText = Math.round(data.main.feels_like)

        currentWeather.temp = Math.round(data.main.temp)
        currentWeather.heatIndex = Math.round(data.main.feels_like)
    })

// Code running down here

}

console.log(currentWeather)

// Promises: a contract in your code, that promises that a variable will be assigned at some point in the future

// Promise: Pending, Fullfilled, Rejected
