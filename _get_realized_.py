import psycopg2.extras
from controller import RobotRotine as rr
from api import graphqlconsume, querygraphql
import time
import datetime
import numpy as np
import schedule 

def job():
    robo2 = rr.RobotRotine()
    dtfim = np.datetime64(datetime.datetime.now())
    dtinit = np.datetime64(dtfim) - np.timedelta64(110, 'm')
    print('Função Realized')
    print(dtinit)
    print(dtfim)
    print('-')
    robo2.ExecutaRotina('date_realized', dtinit,
                            dtfim, 1)
    print('Periodo Executado com sucesso')


schedule.every(100).minutes.do(job)
print('Esperando o proximo intervalo para executar.......')

while True:
    schedule.run_pending()
    time.sleep(1)