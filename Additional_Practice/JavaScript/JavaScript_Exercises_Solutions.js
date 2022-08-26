// * Exercise 1: Solution and Explanation *

// for(let num = 0; num <= 10; num++) {    //Set up your for loop with your variable = 0, run through while the variable is less than or equal to 10, and increment the variable each time
//     console.log(num)                    //print out the numbers 1-10
// }


// * Exercise 2: Solution and Explanation *

// for(num = 1; num <= 100; num += 2) {    //Setup for loop and assign variable to start at one, and as long as the number is less than 100 keep running through the loop, incrementing by two each time.
//     console.log(num)                    //print out the odd numbers
// }



// * Exercise 3: Solution and Explanation *


// let sumNum = 0;                          // assign the variable sumNum to 0

// for(num = 1; num <= 10; num++) {         //for loop(our variable = 1, keep running this loop as long as our variable is less than or equal to 10, increment the number every time we run through our loop)
//     sumNum += num                        //sumNum = sumNum + num
// };

// console.log(sumNum);                     //print out our solution



// * Exercise 4: Solution and Explanation *

// let sumNum = 0;                          // assign the variable sumNum to 0
// for(num = 11; num <= 30; num+=2){        // for loop(our variable = 11, keep running this loop as long as our variable is less than or equal to 30, increment the number by 2 every time we run through our loop)
//     sumNum += num                        //sumNum = sumNum + num
// };
// console.log(sumNum);                     //print out our solution


// * Exercise 5: Solution and Explanation *

// let sumArr = [1,2,3,4,5,6,7,8,9,10];     // assign the variable sumArr to a list of numbers


// function sumNum(sumArr)                  // set up our function to take in one parameter
// {
//     let sum = 0;                         // assign the variable sum to = 0
    
//     for(let num = 0; num < sumArr.length; num++)     // for loop (assign our variable to = 0, as long as our variable is less than the length of the array then we want our for loop to continue running, each time we go through the for loop we want to increment our variable)
//     {
//         sum += sumArr[num];              // let sum = sum + (number in array according to the[index position of our variable num])
//     }
    
//     console.log(sum);                    // once the loop is complete print out our result
// }


// sumNum(sumArr)                           // call our function and pass in our list


// * Exercise 6: Solution and Explanation *


// let avgArr = [1,2,3,4,5,6,7,8,9,10];     // assign our variable avgArr to a list of numbers

// function average(arr) {                  // set up our function to take in one parameter
//     let avg = 0                          // assign our variable to = 0
    
//     for(let num = 0; num < arr.length; num++){       // for loop(our variable is = 0, as long as our variable is less than the length of the array we pass in then we want our for loop to keep going, and we want our variable to increment each time)
//         avg += arr[num];                 // avg variable now = avg + ourList[index position of num val depending on iteration of the loop]
//     }
//     return (avg / arr.length);           // return our avg divided by the length of the list
    
// }

// let result = average(avgArr)             // Call the function and pass in your list, and store this in the variable result
// console.log(result)                      // Print out your results


// * Exercise 7: Solution and Explanation 1 - The Long Way*


// let numsList = [1,-2,3,-4,5,6,-7,8,9,10];        // assign our variable numsList to a list of numbers

// function posNums(numsList) {                     // set up our function to take in one parameter
//         let posNums = [];                        // assign the variable posNums to an empty list
//         for(let i = 0; i < numsList.length; i++) // for loop(our variable is = 0, as long as our variable is less than the length of the array we pass in then we want our for loop to keep going, and we want our variable to increment each time) 
//         {
//             let num = numsList[i];               // assign the variable num to = ourList[index position incrementing each time we run through our loop]
//             if (num > 0)                        // if our variable is greater than 0 we know that it is a positive number 
//             {
//                 posNums.push(num);               // Take any positive number found and put it in our list that we called posNums
//             }
//         }
//         return posNums;                          // After the loop is complete, return the list of positive numbers that we have created
// }
// let result = posNums(numsList)                   // Call the function and pass in your list, and store this in the variable result
// console.log(result)                              // Print out your results


// * Exercise 7: Solution and Explanation 1 - The Short Way*

// let numsList = [1,-2,3,-4,5,6,-7,8,9,10];        // assign our variable numsList to a list of numbers

// function getPositives(numsList)                  // set up our function to take in one parameter
// {
//     return numsList.filter(nums => nums > 0);   // Using the filter method, we filter through our list. This is a function, saying that (our parameter(nums), =>(arrow function), return any number that is greater than 0)
// }
// let result = getPositives(numsList)             // Call the function and pass in your list, and store this in the variable result
// console.log(result)                              // Print out your results


// * Exercise 8: Solution and Explanation *


// let numList = [1,2,3,4,5,6,17,8,9,10];           // assign our variable numsList to a list of numbers

// function largest(numList) {                      // set up our function to take in one parameter
//     let max = numList[0];                        // assign the variable max to equal the number that is in index 0 of our list
    
//     for(let i = 0; i < numList.length; i++)       // for loop(our variable is = 0, as long as our variable is less than the length of the array we pass in then we want our for loop to keep going, and we want our variable to increment each time) 
//     {
//         if (numList[i] > max)                    // if the number that is found in the index position[i, which will increment each time the loop is run until we have reached the end of the list] is greater than the number stored in our max variable
//         {
//             max = numList[i];                    // then the number that was stored in the max variable is replaced with the new, higher number that was found
//         }
//     }
    
//     return max;                                  // once the for loop is done, return our max number
// }
// let result = largest(numList)                    // Call the function and pass in your list, and store this in the variable result
// console.log(result)                              // Print out your results



// * Exercise 9: Solution and Explanation *


// let arr = [1,2,3,4,5]                            // assign our variable numsList to a list of numbers

// function reversed(arr){                          // set up our function to take in one parameter
//     let newArr = [];                             // assign the varaible newArr to an empty array
    
//     for(let num = arr.length - 1; num >= 0; num--)   // for loop(our variable num is equal to the length of our array minus one, and as long as our number does not get lower than 0 we will keep running our loop, decrementing each time we iterate)
//     {
//         newArr.push(arr[num]);                   // add the number found each time our num variable decrements(first time it will add 5 to our list, then 4, then 3, etc.)
//     }
    
//     return newArr;                               // Once our for loop has run, return the new list that has been stored to our variable newArr
// }

// let result = reversed(arr)                    // Call the function and pass in your list, and store this in the variable result
// console.log(result)                              // Print out your results


// * Exercise 10: Solution and Explanation *


// let str = 'Dezarea Bryan';                   // assign the variable str to a string

// function reversed(str){                      // set up our function to take in one parameter
//     let newStr = ''                          // assign the variable newStr to an empty string
//     for(let word = str.length - 1; word >= 0; word--){      // for loop(our variable word is equal to the length of our array minus one, and as long as our variable word does not have a value that drops below 0 we will keep running our loop, decrementing each time we iterate)
//         let val = str[word]                  // assign the variable val to the letter that is found in our given string[at the index of word, which changes each time we iterate through the loop, giving us our letters in reverse]
//         newStr += val                        // our variable newStr now = newStr + val
//     }
//     return newStr                            // return our newStr
// }

// let result = reversed(str);                    // Call the function and pass in your list, and store this in the variable result
// console.log(result)                              // Print out your results


