import psycopg2.extras
from controller import RobotRotine as rr
from api import graphqlconsume, querygraphql
import time
import datetime
import numpy as np

robo2 = rr.RobotRotine()
dtinit = np.datetime64(datetime.datetime.now())
dtfim = dtinit
while True:
    print(dtinit)
    print(dtfim)
    print('-')
    robo2.ExecutaRotina('created_at', dtinit,
                        dtfim, 1)
    print('Esperando o proximo intervalo para executar.......')
    time.sleep(2700)
    dtinit = dtfim
    dtfim = np.datetime64(datetime.datetime.now())
    dtfim = np.datetime64(dtfim) + np.timedelta64(90, 'm')


print('Periodo Executado com sucesso')
