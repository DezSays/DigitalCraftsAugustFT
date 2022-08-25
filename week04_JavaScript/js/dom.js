



// Rerieves the user input in the input boxes
username = document.getElementById('username-box').value;
password = document.getElementById('password-box').value;
login = document.getElementsByTagName('button');
login.addEventListener('click', checkPassword)
console.log(`Username: ${username}, Password: ${password}`);
checkPassword(username, password);


function checkPassword(username, password) {
    let mockDb = new Map();
    // adding username and password to the db
    mockDb.set('drtaylor', 'test');
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


