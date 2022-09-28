const express = require('express');
const app = express()
const { Sequelize } = require('sequelize')

const sequelize = new Sequelize('postgres://postgres:test@localhost:5432/postgres')

app.use(express.json())
app.set('view engine', 'ejs')

app.get('/students', async function(req,res) {
    const classroom = await students.findAll();
    console.log(classroom)
    res.send(classroom)
})


app.post('/students', async(req,res)  => {

    const student = await students.create({
        first_name: req.body.first_name, 
        last_name: req.body.last_name,
        birthdate: req.body.birthdate,
        grade: req.body.grade
    })
    let receipt = await students.findAll({
        where: {
        first_name: req.body.first_name,
        last_name: req.body.last_name
    }
    })
    res.send(receipt)
})

app.listen(3000, () => {
console.log(`Server is running on http://localhost:3000`) 
})