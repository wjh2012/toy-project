const mongoose = require('mongoose')
const boardSchema = require('../board.schema')

const model = mongoose.model('love', boardSchema)

module.exports = model