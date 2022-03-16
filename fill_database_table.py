#########################################################
#                                                       #
#   Use this file to fill up a given database table     #
#                                                       #
#########################################################

from cProfile import label
import MongoDB.session as ses
import MongoDB.read_collection as read
import PostgreSQL.connect_db as connect

def insert(cursor, table, labels, datapoint):
    """insert one datapoint into table of given cursor
    
    @params
    cursor: cursor corresponding to required connection
    table: name of table ti insert into
    labels: list of strings of database labels
    datapoint: list of data that has to be inserted
    """
    cursor.execute(f'''INSERT INTO {table} ({', '.join(labels)}) VALUES ({('%s,'*len(datapoint))[:-1]})''',  datapoint)


# Use the following two lines to get your collection and said data form the right MongoDB
collection = ses.get_collection(database=ses.get_database(client=ses.get_client(host="Localhost", port=27017), database_name="opisop"), collection_name="products")
collection_data = read.get_collection_information(collection=collection, labels=["_id", "name", ["price", "selling_price"]])

# Use the following line to connect to your PostgreSQL 
connection = connect.connect_db(host='localhost', database='opisop_sql', user='postgres', password='postgres')
cursor = connection.cursor()

for datapoint in collection_data:
    # Make sure the line below represents the correct labels for the data you want to insert 
    insert(cursor=cursor, table='products', labels=['id', 'name', 'price'], datapoint=datapoint)

cursor.close()
connection.commit()
