import psycopg2


def connectdb():
    con = psycopg2.connect(
        host='localhost',
        database='test2',
        user='postgres',
        password='uwu'
    )
    return con

def insert(sql):
    con = connectdb()
    cur = con.cursor()
    cur.execute(sql, ('a', 'b'))
    con.commit()


sql = 'INSERT INTO "testTable" (var1, var2) VALUES(%s, %s)'