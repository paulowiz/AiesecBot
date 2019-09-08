
///execução de query e passa para json
const getTableData = (req, res, db) => {
  db.select('*').from('applications') /* mudar ali para o nome da sua tabela */
    .then(items => {
      if(items.length){
        res.json(items) 
      } else {
        res.json({dataExists: 'false'})
      }
    })
    .catch(err => res.status(400).json({dbError: 'db error'}))
}

const getTableData2 = (req, res, db) => {
  db.select('*').from('entity') /* mudar ali para o nome da sua tabela */
    .then(items => {
      if(items.length){
        res.json(items) 
      } else {
        res.json({dataExists: 'false'})
      }
    })
    .catch(err => res.status(400).json({dbError: 'db error'}))
}


//exibe o retorno do banco em json
module.exports = {
  getTableData,
  getTableData2

}