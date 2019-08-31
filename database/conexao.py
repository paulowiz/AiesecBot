import psycopg2
import psycopg2.extras

class conexao:
       
    def __init__(self,dbname,user,host,password):
      self.dbname = dbname
      self.user =  user
      self.host =  host
      self.password =  password
  
    def conectadb(self):
        try:
            #Efetua a conexao com o banco de dados
            conn = psycopg2.connect("dbname='%s' user='%s' host='%s' password='%s'" % (
               self.dbname,
               self.user,
               self.host,
               self.password 
                ))
            print("Conectado com sucesso.")
            return conn
        except:
            print("Erro ao logar no banco de dados.")
            exit()  
            
    def executaQuery(self,conn,query):
       #conn = conectadb()
       cur = conn.cursor(cursor_factory = psycopg2.extras.RealDictCursor)   
       cur.execute(query)
       conn.commit()
       return print("Registro Salvo com sucesso")
       #cur.close()
       #conn.close()
pass