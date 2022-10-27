
// Three things that every languages have:
// 1. memory heap
// 2. execution context
// 3. call stack


// let count = 0

const counter = () => {
    let count = 0;
    count = count+1

    return count
}

let result = counter() // 1
result = counter() // 1
result = counter() // if global, 1 to start
result = counter() // then 2

class Count {
    constructor(){
        this.count = 0;
    }

    increment(){
        this.count++

        return this.count
    }
}

let count = new Count()
let res = count.increment() // 1
let sol = count.constructor() // 0




const greeting = () => {
    console.log('greetings all')
}

domElement.addEventListener('click', () => {
    
})