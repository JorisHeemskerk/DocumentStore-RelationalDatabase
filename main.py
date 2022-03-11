import MongoDB.session as ses
import MongoDB.read_collection as read
import PostgreSQL.Connect_db as connect

collection = ses.get_collection(ses.get_database(ses.get_client(), "opisop"), "products")
collection_data = read.get_collection_information(collection, ["_id", "name", ["price", "selling_price"]])

con = connect.connectdb('localhost', 'opisop_sql', 'postgres')
cur = con.cursor()

for data in collection_data:
    cur.execute('''INSERT INTO products (id, name, price) VALUES (%s,%s,%s)''',  (data[0], data[1], data[2]))
cur.close()
con.commit()
