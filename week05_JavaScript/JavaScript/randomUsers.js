let userButton = document.getElementById('userButton');
let avatarImage = document.getElementById('avatar-img');
let userTitle = document.getElementById('userTitle');
let message = document.getElementById('overview');

const getUsers = () => {
    fetch('https://random-data-api.com/api/v2/users?size=1')
    .then(response => {
        return response.json();
    })
    .then(userData => {
        console.log(userData);

        // Step 1: Get the user image
        let avatar = userData.avatar;
        console.log(avatar);

        // Step 2: Place the image inside of our card
        avatarImage.src = avatar;

        // Step 3: Set Card Title to username
        let username = userData.username;
        userTitle.innerText = username; 

        // Step 4: Set card data to a introductory message
        message.innerText = 'Hi my name is ' + userData.first_name + ' ' + userData.last_name + ' I am a ' + userData.employment.title;
    })
}