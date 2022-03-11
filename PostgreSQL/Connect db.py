import psycopg2


def connectdb(host,database):
    con = psycopg2.connect(
        host=host,
        user='postgres',
        database=database,
        password='postgres',
    )
    return con