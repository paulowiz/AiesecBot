import psycopg2.extras
import json
import pandas as pd
from pandas.io.json import json_normalize
import pandas.io.json as pd_json
from database.conexao import conexao 
from api import graphqlconsume,querygraphql
from pandas.io.json import json_normalize
import pandas.io.json as pd_json
import datetime


#CONECTA NO BANCO E PERMITE FAZER QUERIES
banco =  conexao("dashboardbf","thaleslopes", "dashboard-bf.cpcjumtjwpk7.us-west-1.rds.amazonaws.com","4568520rds")
conn = banco.conectadb()
            
graphql = graphqlconsume.graphqlConsume()
queryGraphQL = querygraphql.queryGraphql()

queryqg = queryGraphQL.chamaGraphQL()
retorno = graphql.executaGraphQL(queryqg)


data = retorno['allOpportunityApplication']['data']

for reg in data:
    
    if reg['created_at'] is None:
        created_at = ""
    else:
       created_at = datetime.datetime.strptime(reg['created_at'],"%Y-%m-%dT%H:%M:%SZ")
      
    if reg['date_matched'] is None:
        date_matched = ""
    else:
       date_matched = datetime.datetime.strptime(reg['date_matched'],"%Y-%m-%dT%H:%M:%SZ")
       
    if reg['date_approved'] is None:
        date_approved = ""
    else:
       date_approved = datetime.datetime.strptime(reg['date_approved'],"%Y-%m-%dT%H:%M:%SZ")
         
    if reg['experience_start_date'] is None:
        experience_start_date = ""
    else:
       experience_start_date = datetime.datetime.strptime(reg['experience_start_date'],"%Y-%m-%dT%H:%M:%SZ")
       
    if reg['date_realized'] is None:
        date_realized = ""
    else:
       date_realized = datetime.datetime.strptime(reg['date_realized'],"%Y-%m-%dT%H:%M:%SZ")
       
    if reg['experience_end_date'] is None:
       experience_end_date = ""
    else:
       experience_end_date= datetime.datetime.strptime(reg['experience_end_date'],"%Y-%m-%dT%H:%M:%SZ")
         
    if reg['nps_response_completed_at'] is None:
        nps_response_completed_at = ""
    else:
       nps_response_completed_at = datetime.datetime.strptime(reg['nps_response_completed_at'],"%Y-%m-%dT%H:%M:%SZ") 

    if  reg['date_approval_broken'] is None:
        date_approval_broken = ""
    else:   
       date_approval_broken = datetime.datetime.strptime(reg['date_approval_broken'],"%Y-%m-%dT%H:%M:%SZ") 

    query = "INSERT INTO applications(id_application,"
    query +=                    "id_ep,"
    query +=                    "id_opportunity,"
    query +=                    "id_home,"    
    query +=                    "id_host,"
    query +=                    "product,"
    query +=                    "status,"
    query +=                    "applied_at,"              
    query +=                    "accepted_at,"
    query +=                    "approved_at,"
    query +=                    "pred_realized_at,"
    query +=                    "realized_at,"
    query +=                    "finished_at,"
    query +=                    "completed_at,"
    query +=                    "break_approval_at)"
    query += "VALUES('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"  % (reg['id'],
                                                                                                      reg['person']['id'],
                                                                                                      reg['opportunity']['id'],
                                                                                                      reg['person']['home_mc']['id'],
                                                                                                      reg['home_mc']['id'],
                                                                                                      reg['opportunity']['programme']['short_name_display'],
                                                                                                      reg['status'],
                                                                                                      created_at,
                                                                                                      date_matched,
                                                                                                      date_approved,
                                                                                                      experience_start_date,
                                                                                                      date_realized,
                                                                                                      experience_end_date,
                                                                                                      nps_response_completed_at,
                                                                                                      date_approval_broken,
                                                                                                      )
    print(query)
    banco.executaQuery(conn,query)
    
   