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
robo5 = rr.RobotRotine()
i = 0
dtinit = '2019-03-01T00:00:00'
while i < 18:
    print(dtinit)
    dtfim = np.datetime64(dtinit) + np.timedelta64(24, 'h')
    robo5.ExecutaRotina('created_at', dtinit,
                        dtfim, 1)
    i = i+1
    dtinit = np.datetime64(dtinit) + np.timedelta64(24, 'h')

print('Periodo Executado com sucesso')
