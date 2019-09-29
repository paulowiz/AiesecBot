import psycopg2.extras
from controller import RobotRotine as rr
from api import graphqlconsume, querygraphql
import time
import datetime
import numpy as np
"""
current = np.datetime64(datetime.datetime.now())
currentab = np.datetime64(current) + np.timedelta64(5, 'h')
lastdate = np.datetime64(currentab) - np.timedelta64(15, 'm')
print(lastdate)
print(currentab)
print('-')

"""

robo2 = rr.RobotRotine()
dtinit = np.datetime64(datetime.datetime.now())
dtinit = np.datetime64(dtinit) + np.timedelta64(3, 'h')
dtfim = np.datetime64(dtinit) + np.timedelta64(2, 'm')
while True:
    print(dtinit)
    print(dtfim)
    print('-')
    robo2.ExecutaRotina('date_realized', dtinit,
                        dtfim, 1)
    print('Esperando o proximo intervalo para executar.......')
    time.sleep(120)
    dtinit = dtfim
    dtfim = np.datetime64(datetime.datetime.now())
    dtfim = np.datetime64(dtfim) + np.timedelta64(3, 'h')
    dtfim = np.datetime64(dtfim) + np.timedelta64(2, 'm')


print('Periodo Executado com sucesso')