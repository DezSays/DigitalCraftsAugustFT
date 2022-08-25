// * Solution 1 *

// for(let num = 0; num <= 10; num++) {    //Set up your for loop with your variable = 0, run through while the variable is less than or equal to 10, and increment the variable each time
//     console.log(num)                    //print out the numbers 1-10
// }


// * Solution 2 *

// for(num = 1; num <= 100; num += 2) {    //Setup for loop and assign variable to start at one, and as long as the number is less than 100 keep running through the loop, incrementing by two each time.
//     console.log(num)                    //print out the odd numbers
// }



// * Solution 3 *


// let sumNum = 0;

// for(num = 1; num <= 10; num++) {
//     sumNum += num
// };

// console.log(sumNum);



// * Solution 4 *

// let sumNum = 0;
// for(num = 11; num <= 30; num+=2){
//     sumNum += num
// };
// console.log(sumNum);


// * Solution 5 *

// let sumArr = [1,2,3,4,5,6,7,8,9,10];


// function sumNum(sumArr)
// {
//     let sum = 0;
    
//     for(let num = 0; num < sumArr.length; num++)
//     {
//         sum += sumArr[num];
//     }
    
//     console.log(sum);
// }


// sumNum(sumArr)


// * Solution 6 *


// let avgArr = [1,2,3,4,5,6,7,8,9,10];

// function average(arr) {
//     let avg = 0
    
//     for(let num = 0; num < arr.length; num++){
//         avg += arr[num];
//     }
//     return (avg / arr.length);
    
// }

// let result = average(avgArr)
// console.log(result)


// * Solution 7 *


// let numsList = [1,-2,3,-4,5,6,-7,8,9,10];

// Longer solution

// function posNums(numsList) {
//         let posNums = [];
//         for(let i = 0; i < numsList.length; i++)
//         {
//             let num = numsList[i];
//             if (num >= 0)
//             {
//                 posNums.push(num);
//             }
//         }
//         return posNums;
// }
// let result = posNums(numsList)
// console.log(result)



// Shorter solution

// function getPositives(numsList)
// {
//     return numsList.filter(el => el >= 0);
// }
// let result = getPositives(numsList)
// console.log(result)


// * Solution 8 *


// let numList = [1,2,3,4,5,6,17,8,9,10];

// function largest(numList) {
//     let max = numList[0];
    
//     for(let i = 0; i < numList.length; i++)
//     {
//         if (numList[i] > max)
//         {
//             max = numList[i];
//         }
//     }
    
//     return max;
// }
// let result = largest(numList)
// console.log(result)


// * Solution 9 *


// let arr = [1,2,3,4,5]

// function reversed(arr){
//     let newArr = [];
    
//     for(let num = arr.length - 1; num >= 0; num--)
//     {
//         newArr.push(arr[num]);
//     }
    
//     return newArr;
// }

// let result = reversed(arr)
// console.log(result)



// * Solution 10 *


// let str = 'Dezarea Bryan';

// function reversed(str){
//     let newStr = ''
//     for(let word = str.length - 1; word >= 0; word--){
//         let val = str[word]
//         newStr += val
//     }
//     return newStr
// }

// let result = reversed(str);
// console.log(result)


