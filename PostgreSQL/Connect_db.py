import psycopg2

def connectdb(host, database, password):
    con = psycopg2.connect(
        host=host,
        database=database,
        user='postgres',
        password=password
    )
    return con

def insert(sql):
    con = connectdb('localhost', 'opisop_sql', 'postgres')
    cur = con.cursor()
    cur.execute(sql)
    cur.close()
    con.commit()