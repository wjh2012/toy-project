const mongoose = require('mongoose')

const boardSchema = mongoose.Schema(
    {
        title: String,
        contents: String,
        author : String,
    },
    {
        timestamps: true
    }
)
/*
boardSchema.method("toJSON", function() {
    const { __v, _id, ...object } = this.toObject();
    object.id = _id;
    return object;
  });
*/
module.exports = boardSchema