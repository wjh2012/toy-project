const model = require('./model')

exports.create = (req, res) => {
    if (!req.body.title) {
        res.status(400).send({ message: "title can not be empty!" })
        return
    }

    const board = new model({
        title: req.body.title,
        contents: req.body.contents
    })

    board
        .save(board)
        .then(data => {
            res.send(data)
        })
        .catch(err => {
            res.status(500).send({
                message:
                    err.message || 'Board를 생성하는동안 문제가 발생하였습니다'
            })
        })
}

exports.findAll = async (req, res) => {
    const collection = await model.find({})

    res.send(collection)
}

exports.findOne = async (req, res) => {
    const id = req.params.id
    console.log(id)
    const doc = await model.findById(id)

    res.send(doc)
}