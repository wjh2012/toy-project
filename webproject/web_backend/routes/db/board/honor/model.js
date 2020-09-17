const mongoose = require('mongoose')
const boardSchema = require('../board.schema')

const model = mongoose.model('honor', boardSchema)

module.exports = model