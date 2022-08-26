



// Rerieves the user input in the input boxes
// username = document.getElementById('username-box').value;
// password = document.getElementById('password-box').value;
// login = document.getElementsByTagName('button');
// login.addEventListener('click', checkPassword)
// console.log(`Username: ${username}, Password: ${password}`);
console.log(checkUsername('Drtaylor'));
//checkPassword(username, password);


function checkUsername(username) {
    // Checking that our input only uses letters
    let myRegex = /^[A-Za-z0-9]+$/
    return myRegex.test(username)
}


function checkPassword(username, password) {
    let mockDb = new Map();
    // adding username and password to the db
    mockDb.set('drtaylor@mail.com', 'test123');
    mockDb.set('digitalcrafts', 'test2');
    
    

    //Checking to see if the username is in the database
    // Username was not found
    if(mockDb.get(username) == undefined) {
        alert('No account found with that username.')
    // Check if password matches what is in the db
    } else if(mockDb.get(username) == password) {
        alert('You are signed in')
    // Username exists but password is incorrect
    } else {
        alert('Wrong Password.')
    }
}

function createUser(username, password, country) {
    let mockDb = new Map();
    passwordRegex = /[A-Za-z0-9] +/
    // Checks if username length is > 0
    if(username.length == 0) {
        print('Must type in valid username')
    }
    // Checks if password meets minimum combination of characters 
    else if(!passwordRegex.test('password')) {
        print('Must use letters and numbers for password')
    }
    newuser = {'username': username, 'password': password, 'country': country}
}


