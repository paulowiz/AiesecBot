import psycopg2.extras
import json
import pandas as pd
from pandas.io.json import json_normalize
import pandas.io.json as pd_json
from database.conexao import conexao 
from api import graphqlconsume,querygraphql
from pandas.io.json import json_normalize
import pandas.io.json as pd_json


#CONECTA NO BANCO E PERMITE FAZER QUERIES
banco =  conexao("dashboardbf","thaleslopes", "dashboard-bf.cpcjumtjwpk7.us-west-1.rds.amazonaws.com","4568520rds")
conn = banco.conectadb()
            
graphql = graphqlconsume.graphqlConsume()
queryGraphQL = querygraphql.queryGraphql()

queryqg = queryGraphQL.chamaGraphQL()
retorno = graphql.executaGraphQL(queryqg)


data = retorno['allOpportunityApplication']['data']

for reg in data:
    query = "INSERT INTO TESTE(user_dsc,grant_date)VALUES('%s','%s')" % (reg['id'],reg['created_at'])
    print(query)
    banco.executaQuery(conn,query)
    
   