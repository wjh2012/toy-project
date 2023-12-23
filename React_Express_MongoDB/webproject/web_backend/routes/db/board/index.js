const express = require('express')
const router = express.Router()

const free = require('./free/routes')
const love = require('./love/routes')
const school = require('./school/routes')
const honor = require('./honor/routes')
const eat = require('./eat/routes')

router.use('/free',free)
router.use('love',love)
router.use('/school',school)
router.use('/honor',honor)
router.use('/eat',eat)

module.exports = router