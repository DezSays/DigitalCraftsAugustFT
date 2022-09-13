let axios = require('axios').default; 
let http = require('http');

const host = '127.0.0.1'
const port = 8080
const anotherPort = 8001

const server = http.createServer((req,res) => {
    res.statusCode = 200;
    res.setHeader('Content-Type', 'text/plain');
    res.end(`You've reached my server`);
});


server.listen(port, host, () => {
    console.log(`Server is running at http:${host}:${port}`)
});

const anotherServer = http.createServer((req, res) => {
    res.statusCode = 200
    res.setHeader('Content-Type', 'text/plain');
    res.end(`You've reached my server #2`);
})


anotherServer.listen(anotherPort, host, () => {
    console.log(`Server is running at http:${host}:${anotherPort}`)
});