import psycopg2.extras
from controller import RobotRotine as rr
from api import graphqlconsume, querygraphql

robo3 = rr.RobotRotine()

robo3.ExecutaRotina('date_approved', '2017-01-01T00:00:01Z',
                    '2017-06-30T23:59:59Z', 26)
