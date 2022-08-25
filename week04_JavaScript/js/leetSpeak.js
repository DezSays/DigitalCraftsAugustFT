// leetSpeak using a map 

// let leetSpeak = (userInput) => {

//     let leetMap = new Map();

//     leetMap.set('D', '7');
//     leetMap.set('Z', '6');
//     leetMap.set('R', '5');
//     leetMap.set('Y', '4');
//     leetMap.set('N', '3');

//     let textInput = userInput.toUpperCase().split('');
//     for (i = 0; i < textInput.length; i++) {
//         if (leetMap.get(textInput[i]) == undefined) {
//         continue;
//         }
//         else {
//         textInput[i] = leetMap.get(textInput[i])
//         }
//     }

//     return textInput.join('')
// }

// let text = 'Dezarea Bryan'
// console.log(leetSpeak(text))




// leetSpeak using a switch statement

// const leetspeak = (word) => {
//     let leet = '';
//     for(let i = 0; i < word.length; i++) {
//         switch(word[i].toLowerCase()) {
//             case 'a':
//                 leet += '4';
//                 break;
//             case 'e':
//                 leet += '3';
//                 break;
//             case 'g':
//                 leet += '6';
//                 break;
//             case 'i':
//                 leet += '1';
//                 break;
//             case 'o':
//                 leet += '0';
//                 break;
//             case 's':
//                 leet += '5';
//                 break;
//             case 't':
//                 leet += '7';
//                 break;
//             default:
//                 leet += word[i];
//         }
//     } 
//     return leet; 
// }

// console.log(leetspeak('Dezarea Bryan'))


