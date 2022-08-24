// leetSpeak using a map -- a much shorter solution, but you could also get to the answer other ways

let leetSpeak = (userInput) => {

    let leetMap = new Map();

    leetMap.set('D', '7');
    leetMap.set('Z', '6');
    leetMap.set('R', '5');
    leetMap.set('Y', '4');
    leetMap.set('N', '3');

    let textInput = userInput.toUpperCase().split('');
    for (i = 0; i < textInput.length; i++) {
        if (leetMap.get(textInput[i]) == undefined) {
        continue;
        }
        else {
        textInput[i] = leetMap.get(textInput[i])
        }
    }

    return textInput.join('')
}

let text = 'Dezarea Bryan'
console.log(leetSpeak(text))