#########################################################
#                                                       #
#   Use this file to fill up a given database table     #
#                                                       #
#########################################################

import MongoDB.session as ses
import MongoDB.read_collection as read
import PostgreSQL.connect_db as connect

# Use the following two lines to get your collection and said data form the right MongoDB
collection = ses.get_collection(database=ses.get_database(client=ses.get_client(host="Localhost", port=27017), database_name="opisop"), collection_name="products")
collection_data = read.get_collection_information(collection=collection, labels=["_id", "name", ["price", "selling_price"]])

# Use the following line to connect to your PostgreSQL 
connection = connect.connect_db(host='localhost', database='opisop_sql', user='postgres', password='postgres')
cursor = connection.cursor()

for datapoint in collection_data:
    # Make sure the line below represents the correct values (in the right SQL format) for the data you want to insert 
    cursor.execute('''INSERT INTO products (id, name, price) VALUES (%s,%s,%s)''',  (datapoint[0], datapoint[1], datapoint[2]))

cursor.close()
connection.commit()
