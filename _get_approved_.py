import psycopg2.extras
from controller import RobotRotine as rr
from api import graphqlconsume, querygraphql
import time
import datetime
import numpy as np
# TAKE SYSDATE + 60 MINUTES TO EXECUTE ALL ROUTINE.
robo2 = rr.RobotRotine()
dtinit = np.datetime64(datetime.datetime.now())
dtfim = dtinit
while True:
    print(dtinit)
    print(dtfim)
    print('-')
    robo2.ExecutaRotina('date_approved', dtinit,
                        dtfim, 1)
    print('Esperando o proximo intervalo para executar.......')
    time.sleep(3600)
    dtinit = dtfim
    dtfim = np.datetime64(datetime.datetime.now())
    dtfim = np.datetime64(dtfim) + np.timedelta64(60, 'm')


print('Periodo Executado com sucesso')
