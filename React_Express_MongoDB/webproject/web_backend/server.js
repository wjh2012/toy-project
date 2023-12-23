const express = require('express')
const app = express()

const db = require('./db')
db()

// body-parser는 express에 자체 내장되어있으므로 설치 필요 X
app.use(express.json())
app.use(express.urlencoded({ extended: true }))

const routes = require('./routes')
app.use('/', routes)

const PORT = 3001;
app.listen(PORT, () => {
    console.log('server is running on port' + PORT)
})