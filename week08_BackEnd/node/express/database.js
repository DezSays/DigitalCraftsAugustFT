// // Mock db for right now
// let pokedex = [{"name": 'pikachu', 'hp': 50}, {"name": 'bulbasaur', 'hp': 40}, {"name": 'charmander', 'hp': 50}]

// module.exports = pokedex;

import postgres from 'postgres'

const sql = postgres({}) // will use psql environment variables

export default sql