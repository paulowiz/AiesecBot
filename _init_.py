import psycopg2.extras
from controller import RobotRotine as rr
from api import graphqlconsume, querygraphql

robo1 = rr.RobotRotine()

robo1.ExecutaRotina('date_approved', '2019-09-20T00:00:01Z',
                    '2019-09-26T00:00:01Z', 1)
