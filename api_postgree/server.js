const express = require('express')

require('dotenv').config()


const helmet = require('helmet') 
const bodyParser = require('body-parser') 
const cors = require('cors') 
const morgan = require('morgan')


/* Aqui voce tem que mecher e bota o seu */
var db = require('knex')({
  client: 'pg',
  connection: {
    host : 'dashboard-bf.cpcjumtjwpk7.us-west-1.rds.amazonaws.com',
    user : 'thaleslopes',
    password : '4568520rds',
    database : 'dashboardbf'
  }
});

const main = require('./controllers/main')


const app = express()


const whitelist = ['http://localhost:3000'] /* Não precisa mecher nisso daki */
const corsOptions = {
  origin: function (origin, callback) {
    if (whitelist.indexOf(origin) !== -1 || !origin) {
      callback(null, true)
    } else {
      callback(new Error('Erro no front'))
    }
  }
}
app.use(helmet())
app.use(cors(corsOptions))
app.use(bodyParser.json())
app.use(morgan('combined')) 

app.get('/', (req, res) => res.send('<font color="red">HELLOW DOS WORDSZAO </font>'))
app.get('/crud', (req, res) => main.getTableData(req, res, db))
app.get('/crud2', (req, res) => main.getTableData2(req, res, db))


app.listen(process.env.PORT || 5000, () => {
  console.log(`app is running on port ${process.env.PORT || 5000}`)
})