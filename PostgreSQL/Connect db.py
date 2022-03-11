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
    con = connectdb('localhost', 'test2', 'uwu')
    cur = con.cursor()
    cur.execute(sql, ('c', 'c'))
    con.commit()


sql = 'INSERT INTO "testTable" (var1, var2) VALUES(%s, %s)'
insert(sql)