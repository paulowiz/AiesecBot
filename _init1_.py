import psycopg2.extras
from controller import RobotRotine as rr
from api import graphqlconsume, querygraphql

robo2 = rr.RobotRotine()


robo2.ExecutaRotina('date_approved', '2016-07-20T00:00:01Z',
                    '2016-12-31T23:59:59Z', 10)
