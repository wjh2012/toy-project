const express = require('express')
const router = express.Router()

router.get('/test', (req, res) => {
    const data = {
        title: 'GGOMJANG',
        contents: 'localhost:3001/api/db/test'
    }
    res.json(data)
    console.log('test send')
})

const board = require('./board')
router.use('/board', board)

module.exports = router