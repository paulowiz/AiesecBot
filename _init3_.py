import psycopg2.extras
from controller import RobotRotine as rr
from api import graphqlconsume, querygraphql

robo4 = rr.RobotRotine()

robo4.ExecutaRotina('date_approved', '2017-07-01T00:00:01Z',
                    '2017-12-30T23:59:59Z', 1)
