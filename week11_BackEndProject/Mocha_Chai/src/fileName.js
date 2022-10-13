
const numbers = [1,5,7]
const words = 'hello dear'



// * Simple function to give us the sum of an array of numbers

function sumFunc(numbers) {
    let sum = 0
    for(let i = 0; i < numbers.length; i++){
        sum += numbers[i]
    }
    return sum
}



