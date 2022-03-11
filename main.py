import MongoDB.session as ses
import MongoDB.read_collection as read
import PostgreSQL.connect_db as con

collection = ses.get_collection(ses.get_database(ses.get_client(), "opisop"), "products")
collection_data = read.get_collection_information(collection, ["_id", "name", ["price", "selling_price"]])

for data in collection_data:
    sql = f'INSERT INTO "products" (id, name, price) VALUES({", ".join(data)})'
con.insert(sql)
