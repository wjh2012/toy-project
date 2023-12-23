const mongoose = require('mongoose')
const boardSchema = require('../board.schema')

const model = mongoose.model('eat', boardSchema)

module.exports = model