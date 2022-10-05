// * PROMPT: Create a webpage that creates a new user for an app. The page should take the user's first and last name, email, and address(street, zip, state). Collect this info and store it in a database 

const express = require('express')
const bodyParser = require('body-parser')
const app = express()
app.set('view engine', 'ejs')
const { users } = require('./models')

app.use(bodyParser.urlencoded({ extended: false }))

app.get('/', (req, res)=> {
    res.render("signup")
})

app.post('/createuser', async (req, res) => {
    await users.create({
        firstname: req.body.firstname,
        lastname: req.body.lastname,
        email: req.body.email,
        address: req.body.address
    })
    res.redirect('/')
})

app.listen(3000, console.log('Server running on port 3000'))