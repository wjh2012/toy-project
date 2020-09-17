const express = require('express')
const router = express.Router()
const board = require('./controller')

router.post("/", board.create)

module.exports = router