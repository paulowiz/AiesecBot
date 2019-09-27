import psycopg2.extras
from controller import RobotRotine as rr
from api import graphqlconsume, querygraphql

robo1 = rr.RobotRotine()

robo1.ExecutaRotina('date_approved', '2016-01-20T00:00:01Z',
                    '2016-06-30T23:59:59Z', 3)
