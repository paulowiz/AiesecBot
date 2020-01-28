import psycopg2.extras
import json
import pandas as pd
from pandas.io.json import json_normalize
import pandas.io.json as pd_json
from database.conexao import conexao
from api import graphqlconsume, querygraphql
from pandas.io.json import json_normalize
import pandas.io.json as pd_json
import datetime
import time
import os
from dotenv import load_dotenv
### THE ROUTINE BELOW TAKE ALL INFORMATION FROM EXPA DATABASE(aiesec.org)
## AND SABE ON YOUR LOCAL DATABASE 

#THIS ROUTINE WORKS WITH FOUR TABLES (APPLICATIONS,ENTITY,MC,OPPORTUNITY)

class RobotRotine:

    def __init__(self):
        #self.name = name
        print('O Robo está processando....')

    def ExecutaRotina(self, tp_data, dt_from, dt_to, page):
        # CONECTA NO BANCO E PERMITE FAZER QUERIES
        load_dotenv()
        DB_DATABASE = os.getenv("DB_DATABASE")
        DB_USER = os.getenv("DB_USER")
        DB_HOST = os.getenv("DB_HOST")
        DB_PASSWORD = os.getenv("DB_PASSWORD")
        
        banco = conexao(DB_DATABASE, DB_USER,
                       DB_HOST, DB_PASSWORD)
        try:
            conn = banco.conectadb()
        except:
            return print('Erro ao conectar no banco de dados')
        
        graphql = graphqlconsume.graphqlConsume()
        queryGraphQL = querygraphql.queryGraphql()
        queryqg = queryGraphQL.chamaGraphQL(tp_data, dt_from, dt_to, page)
        try:
            retorno = graphql.executaGraphQL(queryqg)
        except:
            return print('Erro ao executar query GraphQL')
        
        totpages = retorno['allOpportunityApplication']['paging']['total_pages']
        item = 1
        i = page
        while totpages > 0:

            # CONECTA NO BANCO E PERMITE FAZER QUERIES
            retorno = graphql.executaGraphQL(queryqg)
            data = retorno['allOpportunityApplication']['data']
            datapage = retorno['allOpportunityApplication']['paging']

            for reg in data:
                #print(item)
                temid = False
                consultapl = banco.consultaApplication(conn, reg['id'])
                if consultapl is not None:
                    #item = item + 1
                    temid = True
                    # continue

                if reg['created_at'] is None:
                    created_at = "Null"
                else:
                    created_at = datetime.datetime.strptime(
                        reg['created_at'], "%Y-%m-%dT%H:%M:%SZ")
                    created_at = "'%s'" % created_at

                if reg['date_matched'] is None:
                    date_matched = "Null"
                else:
                    date_matched = datetime.datetime.strptime(
                        reg['date_matched'], "%Y-%m-%dT%H:%M:%SZ")
                    date_matched = "'%s'" % date_matched

                if reg['date_approved'] is None:
                    date_approved = "Null"
                else:
                    date_approved = datetime.datetime.strptime(
                        reg['date_approved'], "%Y-%m-%dT%H:%M:%SZ")
                    date_approved = "'%s'" % date_approved

                if reg['experience_start_date'] is None:
                    experience_start_date = "Null"
                else:
                    experience_start_date = datetime.datetime.strptime(
                        reg['experience_start_date'], "%Y-%m-%dT%H:%M:%SZ")
                    experience_start_date = "'%s'" % experience_start_date

                if reg['date_realized'] is None:
                    date_realized = "Null"
                else:
                    date_realized = datetime.datetime.strptime(
                        reg['date_realized'], "%Y-%m-%dT%H:%M:%SZ")
                    date_realized = "'%s'" % date_realized

                if reg['experience_end_date'] is None:
                    experience_end_date = "Null"
                else:
                    experience_end_date = datetime.datetime.strptime(
                        reg['experience_end_date'], "%Y-%m-%dT%H:%M:%SZ")
                    experience_end_date = "'%s'" % experience_end_date

                if reg['nps_response_completed_at'] is None:
                    nps_response_completed_at = "Null"
                else:
                    nps_response_completed_at = datetime.datetime.strptime(
                        reg['nps_response_completed_at'], "%Y-%m-%dT%H:%M:%SZ")
                    nps_response_completed_at = "'%s'" % nps_response_completed_at

                if reg['date_approval_broken'] is None:
                    date_approval_broken = "Null"
                else:
                    date_approval_broken = datetime.datetime.strptime(
                        reg['date_approval_broken'], "%Y-%m-%dT%H:%M:%SZ")
                    date_approval_broken = "'%s'" % date_approval_broken

                if reg['opportunity']['created_at'] is None:
                    opp_created_at = "Null"
                else:
                    opp_created_at = datetime.datetime.strptime(
                        reg['opportunity']['created_at'], "%Y-%m-%dT%H:%M:%SZ")
                    opp_created_at = "'%s'" % opp_created_at

                if reg['opportunity']['sub_product'] is None:
                    sub_product = "Null"
                else:
                    sub_product = "'%s'" % reg['opportunity']['sub_product']['name']

                if reg['opportunity']['duration'] is None:
                    duration = "Null"
                else:
                    duration = "'%s'" % reg['opportunity']['duration']

                if reg['person']['home_mc'] is None:
                    print('Registro com mc_home inválido!')
                    continue
                else:
                    if reg['person']['home_mc']['id'] is None:
                        p_home_mc = "Null"
                    else:
                        p_home_mc = "'%s'" % reg['person']['home_mc']['id']

                if reg['home_mc'] is None:
                    print('Registro com mc_home inválido!')
                    continue
                else:
                    if reg['home_mc']['id'] is None:
                        home_mc = "Null"
                    else:
                        home_mc = "'%s'" % reg['home_mc']['id']

                query = "INSERT INTO applications(id_application,"
                query += "id_ep,"
                query += "id_opportunity,"
                query += "id_home,"
                query += "id_host,"
                query += "product,"
                query += "status,"
                query += "applied_at,"
                query += "accepted_at,"
                query += "approved_at,"
                query += "pred_realized_at,"
                query += "realized_at,"
                query += "finished_at,"
                query += "completed_at,"
                query += "break_approval_at,"
                query += "lc_home)"
                query += "VALUES('%s',%s,'%s',%s,%s,'%s','%s',%s,%s,%s,%s,%s,%s,%s,%s,'%s')" % (reg['id'],
                                                                                                reg['person']['id'],
                                                                                                reg['opportunity']['id'],
                                                                                                p_home_mc,
                                                                                                home_mc,
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
                                                                                                reg['person']['home_lc']['id'])
                queryup = "UPDATE applications SET "
                queryup += "status= '%s'," % reg['status']
                queryup += "applied_at= %s," % created_at
                queryup += "accepted_at= %s," % date_matched
                queryup += "approved_at= %s," % date_approved
                queryup += "pred_realized_at= %s," % experience_start_date
                queryup += "realized_at= %s," % date_realized
                queryup += "finished_at= %s," % experience_end_date
                queryup += "completed_at= %s," % nps_response_completed_at
                queryup += "break_approval_at= %s" % date_approval_broken
                queryup += " where id_application= '%s'" % reg['id']

                # Valida se existe o mc e o lc nas tabelas e somente salva se realmente não tiver
                if reg['person']['home_mc']['id'] is not None:
                    try:
                        consultmc = banco.consultaMc(
                            conn, reg['person']['home_mc']['id'])
                    except:
                        return print('Erro ao consultar MC')
                    if consultmc is None:
                        person_homemc_name = reg['person']['home_mc']['name']
                        person_homemc_name = person_homemc_name.replace(
                            "'", "")
                        query_mc_1 = "INSERT INTO mc(mc_id,mc_dsc)"
                        query_mc_1 += "VALUES(%s,'%s')" % (
                            reg['person']['home_mc']['id'], person_homemc_name)
                        try:
                            banco.executaQuery(conn, query_mc_1)
                            #print('insert do MC realizado com sucesso!')
                        except:
                            return print('Erro ao inserir MC')
                        
                if reg['home_mc'] is not None:
                    try:
                        consultmc = banco.consultaMc(conn, reg['home_mc']['id'])
                    except:
                        return print('Erro ao consultar MC')
                    if consultmc is None:
                        homemc_name = reg['home_mc']['name']
                        homemc_name = homemc_name.replace("'", "")
                        query_mc_2 = "INSERT INTO mc(mc_id,mc_dsc)"
                        query_mc_2 += "VALUES(%s,'%s')" % (
                            reg['home_mc']['id'], homemc_name)
                        try:
                            banco.executaQuery(conn, query_mc_2)
                            #print('insert do MC realizado com sucesso!')
                        except:
                            return print('Erro ao inserir MC')
                        
                try:
                    consultentity = banco.consultaEntity(
                    conn, reg['host_lc']['id'])
                except:
                    return print('Erro ao consultar Entity')
                if consultentity is None:
                    hostlc_name = reg['host_lc']['name']
                    hostlc_name = hostlc_name.replace("'", "")
                    query_entity_1 = "INSERT INTO entity(lc_id,lc_dsc,mc_id)"
                    query_entity_1 += "VALUES(%s,'%s',%s)" % (reg['host_lc']['id'],
                                                              hostlc_name,
                                                              reg['home_mc']['id'])
                    try:
                        banco.executaQuery(conn, query_entity_1)
                        #print('insert do LC realizado com sucesso!')
                    except:
                        return print('Erro ao salvar Entity!')
                try:
                    consultentity = banco.consultaEntity(
                    conn, reg['person']['home_lc']['id'])
                except:
                    return print('Erro ao consultar Entity')
                
                if consultentity is None:
                    person_homelc_name = reg['person']['home_lc']['name']
                    person_homelc_name = person_homelc_name.replace("'", "")
                    query_entity_2 = "INSERT INTO entity(lc_id,lc_dsc,mc_id)"
                    query_entity_2 += "VALUES(%s,'%s',%s)" % (
                        reg['person']['home_lc']['id'], person_homelc_name, reg['person']['home_mc']['id'])
                    try:
                        banco.executaQuery(conn, query_entity_2)
                        #print('insert do LC realizado com sucesso!')
                    except:
                        return print('Erro ao inserir Entity')
                try:
                    consultaOpp = banco.consultaOpp(conn, reg['opportunity']['id'])
                except:
                    return print('Erro ao consultar a oportunidade')
                
                if consultaOpp is None:
                    title = reg['opportunity']['title']
                    title = title.replace("'", "")
                    query_opp = "INSERT INTO opportunity (id,title,created_at,available_openings,duration,subproduct,product,host_lc,host_mc)"
                    query_opp += "VALUES('%s','%s',%s,'%s',%s,%s,'%s','%s',%s)" % (reg['opportunity']['id'],
                                                                                   title,
                                                                                   opp_created_at,
                                                                                   reg['opportunity']['available_openings'],
                                                                                   duration,
                                                                                   sub_product,
                                                                                   reg['opportunity']['programme']['short_name_display'],
                                                                                   reg['host_lc']['id'],
                                                                                   home_mc)
                    try:
                        banco.executaQuery(conn, query_opp)
                    except:
                        print('Ocorreu um erro ao salvar a opp da applicacao: %s e opp %s' % (
                            reg['id'], reg['opportunity']['id']))
                        continue
                if temid is False:
                    banco.executaQuery(conn, query)
                    #print('insert da aplicação realizado com sucesso!')
                else:
                    banco.executaQuery(conn, queryup)
                    #print('update da aplicação realizado com sucesso!')

                item = item + 1
            #print(retorno['allOpportunityApplication']
             #     ['paging']['total_pages'])
            #print(retorno['allOpportunityApplication']
             #     ['paging']['current_page'])
            totpages = totpages - 1
            if totpages <= 0:
                #print('Processo finalizado!')
                print('Foram processados '+str(i)+' pagina(s) e '+str(item)+' Registro(s)')
                exit
            i = i+1
            queryqg = queryGraphQL.chamaGraphQL(tp_data, dt_from, dt_to, i)
        return


pass
