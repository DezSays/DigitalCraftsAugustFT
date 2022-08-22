// When given two strings from the user, write a function that checks if each string is an anagram of the other. If yes, return true, otherwise false

function isAnagram(a, b) {
    let len1 = a.length;
    let len2 = b.length;
    
    if(len1 !== len2){
       console.log('Length of words are not equal');
       return
    }
    let str1 = a.split('').sort().join('');
    let str2 = b.split('').sort().join('');

    let str1Val = str1.toUpper;
    let str2Val = str2.toUpper;

    if(str1Val === str2Val){
       console.log("True");
    } else { 
       console.log("False");
    }
 }
 isAnagram("dog","God")