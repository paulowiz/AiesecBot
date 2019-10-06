import psycopg2.extras
from controller import RobotRotine as rr
from api import graphqlconsume, querygraphql
import time
import datetime
import numpy as np

robo2 = rr.RobotRotine()
dtinit = np.datetime64(datetime.datetime.now())
#dtinit = np.datetime64(dtinit) + np.timedelta64(3, 'h')
dtfim = dtinit  # + np.timedelta64(30, 'm')
while True:
    print(dtinit)
    print(dtfim)
    print('-')
    robo2.ExecutaRotina('date_matched', dtinit,
                        dtfim, 1)
    print('Esperando o proximo intervalo para executar.......')
    time.sleep(1800)
    dtinit = dtfim
    dtfim = np.datetime64(datetime.datetime.now())
   # dtfim = np.datetime64(dtfim) + np.timedelta64(3, 'h')
    dtfim = np.datetime64(dtfim) + np.timedelta64(30, 'm')


print('Periodo Executado com sucesso')
