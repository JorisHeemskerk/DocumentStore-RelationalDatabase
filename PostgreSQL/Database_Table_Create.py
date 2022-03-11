import connect_db

con = connect_db.connectdb('localhost','opisop_sql','password')

def create_table(name, column_strings):
    sql_statement = f'CREATE TABLE {name} (' + ','.join(column_strings) + ')'

    return sql_statement

def create_colum_string(name, type, etc):
    column_string = f'{name} {type} {etc}'
    return column_string

columns = [
    ['id', 'VARCHAR(32)', 'NOT NULL'],
    ['name', 'VARCHAR(256)', ''],
    ['price', 'INT', '']
]

column_list = []
for i in columns:
    column_list.append(create_colum_string(i[0], i[1], i[2]))

sql_statement = create_table('products', column_list)

cur = con.cursor()
cur.execute(sql_statement)
cur.close()
con.commit()
