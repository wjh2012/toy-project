const mongoose = require('mongoose')
const boardSchema = require('../board.schema')

const model = mongoose.model('free', boardSchema)

module.exports = model