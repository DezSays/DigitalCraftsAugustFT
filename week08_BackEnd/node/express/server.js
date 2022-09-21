// Prompt: using the example given for PUT as well as your knowledge of API methods, complete the remaining 3 endpoints, modifying the list accordingly


// Express allows us to create a server that can host an API. We are hosting the API
// on localhost(127.0.0.1)
const express = require('express')
const app = express()
// By default express server cannot read request body in json so we need to add this function to enable that feature  
app.use(express.json())

let pokedex = [{"name": 'pikachu', 'hp': 50}, {"name": 'bulbasaur', 'hp': 40}, {"name": 'charmander', 'hp': 50}]


// An
// Get all pokemon from the pokdex
app.get('/', function (request, response) {
  response.send(pokedex)
})


// GET should always take parameters as a query (ie. /pokemon/?pikachu)
app.get('/pokemon', function (request, response) {
    let pokemon = request.query.name
    for(let i = 0; i < pokedex.length; i++) {
      if(pokedex[i].name == pokemon) {
        hp = pokedex[i].hp
        response.send(pokedex[i]);
      }
    }
    response.send(`${pokemon} does not exist.`)
  })

// Fiona
// Adding a resource to the database
// Path parameters are added to the end of the uri and is taken by the API and used to specify which resource in the db we are refering to. 
//*NOTE* NOT ALL ENDPOINTS USE PATH PARAMETERS

// POST endpoints should be adding resources to the db. It should do this by passing the new resource to be added in the body of the request
app.post('/pokemon', (req,res) => {
    newPokeObject = {"name": req.body.name, "hp": req.body.hp}
    pokedex.push(newPokeObject)
    res.send(`Added ${newPokeObject.name} with an HP of ${newPokeObject.hp} to the Pokedex.`);
})
  

// Modifies a resource that already exists by replacing the entire contents
// I.E({Pokemon: Pikachu, HP: 40} -> {Pokemon: Pikachu, HP: 50})

// In a PUT, place fields to be updated in the request body
app.put('/pokemon/:name', (request, response)=> {
    // Case 1: Check if the HP value is positive and within a reasonable range
    if (request.body.hp <= 10 || request.body.hp > 250) {
        response.statusCode = 400
        response.send(`HP value is not valid`)
    }

    // Case 2: Check the type of hp is not a number
    if(typeof(request.body.hp) != 'number'){
        response.statusCode = 400
        response.send(`HP value is not valid`)
    }

    let pokemon = request.params.name;
    let updated = {}
    for(let i = 0; i < pokedex.length; i++) {
        // Check if the name of the pokemon in the request is in the db
        if(pokedex[i].name == pokemon) {
            // Update pokemon's hp to the requested value and round it to the nearest whole number
            pokedex[i].hp = Math.round(request.body.hp)
            updated = pokedex[i]
        }
    }
    // Send a receipt to the client of exactly what we changed in the db
    response.send(updated);
})

// Wes
// Deletes the resource from the database
// Pass parameters to DELETE as a path parameter
app.delete('/pokemon/:name', (request, response) => {
    // Case 1: Check if the pokemon exists in the db 
    
  let name = request.params.name
  // Checking if pokemon is in the db
  for (let index = 0; index < pokedex.length; index++) {
    if(pokedex[index].name == name){
      deletedPokemon = pokedex[index]
      pokedex.splice(index,1)
      response.send(deletedPokemon)
    }
  }

  response.statusCode = 400
  response.send("pokemon not found")
})

app.listen(3000)
console.log("Server is running on port 3000") 