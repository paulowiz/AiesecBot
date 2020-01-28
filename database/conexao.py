import psycopg2
import psycopg2.extras
# CLASS THAT YOU USE TO CONNECT ON POSTGRESQL DATABASE


class conexao:

    def __init__(self, dbname, user, host, password):
        self.dbname = dbname
        self.user = user
        self.host = host
        self.password = password

    def conectadb(self):
        try:
            # Efetua a conexao com o banco de dados
            conn = psycopg2.connect("dbname='%s' user='%s' host='%s' password='%s'" % (
                self.dbname,
                self.user,
                self.host,
                self.password
            ))
            #print("Conexão com o banco realizada com sucesso!.")
            return conn
        except:
            print("Erro ao logar no banco de dados.")

    def executaQuery(self, conn, query):
        #conn = conectadb()
        # print(query)
        cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        cur.execute(query)
        conn.commit()
        # return print("Registro Salvo com sucesso")
        # cur.close()
        # conn.close()

    def consultaMc(self, conn, mcid):
        cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        query = "SELECT mc_id FROM mc WHERE mc_id = %s LIMIT 1" % mcid
        cur.execute(query)
        recset = cur.fetchall()
        for rec in recset:
            return (rec)

    def consultaOpp(self, conn, oppid):
        cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        query = "SELECT id FROM opportunity WHERE id = %s LIMIT 1" % oppid
        cur.execute(query)
        recset = cur.fetchall()
        for rec in recset:
            return (rec)

    def consultaEntity(self, conn, entid):
        cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        query = "SELECT lc_id FROM entity WHERE lc_id =  %s LIMIT 1" % entid
        cur.execute(query)
        recset = cur.fetchall()
        for rec in recset:
            return (rec)

    def consultaApplication(self, conn, aplid):
        cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        query = "SELECT id_application FROM applications where id_application =  %s LIMIT 1" % aplid
        cur.execute(query)
        recset = cur.fetchall()
        for rec in recset:
            return (rec)


pass
