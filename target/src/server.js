const http = require('http')
const express = require('express')
require('express-async-errors')
const morgan = require('morgan')
const cors = require('cors')

const { routes } = require('./routes')

const app = express()
const server = http.createServer(app)

app.use(express.json())
app.use(morgan('dev'))
app.use(cors())
app.use(routes)
app.use(
  '*',
  (req, res) =>
    res.status(404).json({ message: 'This route is not provided by server' })
)
app.use((err, req, res, next) => {
  console.log(err)
  return res.status(500).json({ message: 'Internal server error' })
})

const shutdown = () => {
  server.close()
  process.exit(0)
}
process.on('SIGINT', shutdown)
process.on('SIGTERM', shutdown)

const start = async () => {
  try {
    server.listen(5000, () => console.log('Server is running on port 5000'))
  } catch (error) {
    console.log(error)
    process.exit(1)
  }
}
start()
