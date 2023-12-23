const mongoose = require('mongoose')
const boardSchema = require('../board.schema')

const model = mongoose.model('school', boardSchema)

module.exports = model