const express = require('express')
const router = express.Router()

const main = require('./main')
const user = require('./users')
const db = require('./db')

router.use('/api/main', main)
router.use('/api/user', user)
router.use('/api/db', db)

// 기본 페이지
router.get('/', (req, res) => {
    res.send('hello server')
})

module.exports = router