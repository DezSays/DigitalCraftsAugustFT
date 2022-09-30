const express = require('express');
const app = express();
const { Sequelize } = require('sequelize');
const { students } = require('./models')

const sequelize = new Sequelize('postgres://postgres:test@localhost:5432/postgres')

app.use(express.json())


// Get all students from the database
app.get('/students', async function(req, res) {
    // Find all students
    const classroom = await students.findAll();
    console.log(classroom)
    res.send(classroom)
})

// Add a student to the database
app.post('/students', async(req, res) => {
    console.log(req.body);
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

app.listen(3000, async () => {
    console.log('Server is running on http://localhost:3000');

    try {
        await sequelize.authenticate();
        console.log('Connection has been established successfully.');
      } catch (error) {
        console.error('Unable to connect to the database:', error);
      }
});