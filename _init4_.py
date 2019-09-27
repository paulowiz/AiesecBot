import psycopg2.extras
from controller import RobotRotine as rr
from api import graphqlconsume, querygraphql

robo4 = rr.RobotRotine()

robo4.ExecutaRotina('date_approved', '2018-07-01T00:00:01Z',
                    '2018-12-30T23:59:59Z', 1)
