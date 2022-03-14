#####################################################################
#                                                                   #
#   Use this file to set up a PostgreSWL database with table(s)     #
#                                                                   #
#####################################################################

import connect_db

def create_table(name, column_strings):
    """Create SQL statement for creating a table containing given columns
    
    @params
    name: name of table
    column_strings: array of table strings (valid SQL format)

    return: string of SQL statment
    """
    sql_statement = f'CREATE TABLE {name} (' + ','.join(column_strings) + ')'
    return sql_statement

def create_column_string(name, type, optional_flags):
    """Create string for given column

    @params
    name: name of column
    type: type for the variables inside column
    optional_flags: optional flags, like NOT NULL etc

    return: joined string of entered items
    """
    return f'{name} {type} {optional_flags}'

def create_columns(columns):
    column_list = []
    for i in columns:
        column_list.append(create_column_string(i[0], i[1], i[2]))



# Use the following line to connect to your PostgreSQL 
connection = connect_db.connectdb(host='localhost', database='opisop_sql', user='postgres', password='password')

# Use the following variable to add all of your required table contents (if no optional flags are wanted, '' is expected to be used)
columns = [
    ['id', 'VARCHAR(32)', 'NOT NULL'],
    ['name', 'VARCHAR(256)', ''],
    ['price', 'INT', '']
]
column_list = create_columns(columns)

# Alter name in case of different table name
sql_statement = create_table(name='products', column_strings=column_list)

cursor = connection.cursor()
cursor.execute(sql_statement)
cursor.close()
connection.commit()
