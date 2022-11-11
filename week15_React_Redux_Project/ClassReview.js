
let weatherInfo= {}

const apiCall = async() =>{
    await fetch('http://api.weatherstack.com/current?access_key=2f2fa67611bbe3f825a9f9920d7e1533&query=New York')
    .then((response) => response.json())
    .then((data) => {
        console.log(data)
        weatherInfo = {
            temparature: data.current.temparature,
            windspeed: data.current.wind_speed,
            description: data.current.weather_description
        }
    })
    // console.log(weatherInfo)
}
apiCall()
