const { Router } = require('express')

const db = require('./database')

const routes = Router()

routes.get('/status', (req, res) => res.json({ ok: true }))
routes.get('/books', async (req, res) => {
  const { rows } = await db.query(`SELECT id, name, description, pages FROM books`)

  const result = rows.map(row => ({
    id: row.id,
    name: row.name,
    description: row.description || '',
    pages: row.pages,
  }))

  return res.json(result)
})

module.exports = { routes }
