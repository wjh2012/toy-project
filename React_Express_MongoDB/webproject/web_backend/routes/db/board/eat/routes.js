const express = require('express')
const router = express.Router()
const board = require('./controller')

router.post("/", board.create)
router.get("/", board.findAll)
router.get("/:id", board.findOne)

module.exports = router