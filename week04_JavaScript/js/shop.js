const form = document.getElementById('cerealform');
const list = document.getElementById('inStock');
const input = document.getElementById('cereal');

form.addEventListener('submit', function(event) {
    // Stop the webpage from reloading upon submission
    event.preventDefault();
    // create a new element when someone submits a cereal
    const newCereal = document.createElement('li');
    newCereal.innerText = cereal.value;
    list.append(newCereal);
    form.reset();

})