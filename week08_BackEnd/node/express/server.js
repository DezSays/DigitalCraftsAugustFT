// Express allows us to create a server that can host an API.
// Express is just the server related material. If you type a . after app, only server methods will pop up because only server methods are in the express library.
// Node is what we are using to run the code, it doesn't have anything to do with the server itself.
// http://localhost:127.0.0.1
const express = require('express');
const app = express()
const PORT = 3333

let pokedex = [{"name":"pikachu", 'hp': 50}, {"name":"bulbasaur", 'hp': 40}, {"name":"charmander", 'hp': 60}]

app.get('/', function (req, res) {
    res.send('You are at the GET endpoint.')
})

//A post method adds a resource to the database

app.post('/pokemon', (req,res) => {
    
    res.send("You created a pokemon.")
})

// Modifies a resource that already exists by replacing the entire contents
// Path parameters are added to the end of the uri and is taken by the API and used to specify which resource in the database we are refering to.
// Note all endpoints use path parameters
app.put('/pokemon/:name', (req,res) => {
    // console.log(req.params.name)
    let pokemon = req.params.name;
    let updatedStat = {name: pokemon, hp: 0}
    for(let i = 0;i < pokedex.length; i++){
        if(pokedex[i].name == pokemon) {
            updatedStat.hp = pokedex[i].hp += 10
        }
    }
    res.send(`Updated ${updatedStat.name}'s hp to ${updatedStat.hp}`)
})

//Deletes the resource from the database. Note, this CANNOT BE UNDONE!
app.delete('/pokemon', (req,res) => {
    res.send('Deleted pokemon.')
})

app.listen(PORT)
console.log(`Running on ${PORT}`)