import psycopg2
import Connect_db

con = Connect_db.connectdb('localhost','opisop_sql','password')


def create_table(name, collum_strings):
    sql_statement = f'CREATE TABLE {name} (' + ','.join(collum_strings) + ')'

    return sql_statement


def create_colum_string(name, type, etc):
    collum_string = f'{name} {type} {etc}'
    return collum_string


collums = [['id', 'VARCHAR(32)', 'NOT NULL'],
           ['name', 'VARCHAR(256)', ''],
           ['price', 'INT', '']
           ]
collum_list = []
for i in collums:
    collum_list.append(create_colum_string(i[0], i[1], i[2]))
sql_statement = create_table('products', collum_list)
cur = con.cursor()
cur.execute(sql_statement)
cur.close()
con.commit()
