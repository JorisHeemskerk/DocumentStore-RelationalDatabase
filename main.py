#############################################################################################
#                                                                                           #
#   This file will excecute all requested excersises laid out in "Formatieve opdracht 2c"   #
#                                                                                           #
#############################################################################################
import PostgreSQL.connect_db as connect

def random_product_id(connection):
    """Retrieve random product id from PostgreSQL database
    
    @params
    connection: A connection to the required database

    return: product id of randomly selected product
    """
    # implement here

def retrieve_products(connection, product_ids):
    """Retrieve products from PostgreSQL database
    
    @params
    connection: A connection to the required database
    product_ids: A list of product ids, by which the products can be found

    return: array of requested products
    """
    products = []
    cursor = connection.cursor()
    for id in product_ids:
        cursor.execute(f"SELECT * from products where id = '{id}'")
        products.append(cursor.fetchall())
    return products

def average_price(products):
    """Calculate average price for given array of products
    
    @params
    products: array of product items

    return: average price
    """
    total = 0
    for product in products:
        total += product[0][2] #3rd item in product is price
    return total/len(products)

def highest_price_difference_product(connection, product_id):
    """find product with highest price difference to given product (corresponding to id) 
    
    @params
    connection: A connection to the required database
    product_id: id, refering to a product item from datbase

    return: the first product with the highest price difference to given product
    """
    # implement here



# initialize connection
connection = connect.connect_db(host='localhost', database='opisop_sql', user='postgres', password='postgres')

#####################################################################################################################################
"""
Formative assignment 2c.1:

The implementation of 2c.1 can be found in fill_database_table.py
This implementation is modular, for more information see MongoDB/read_collection.py, MongoDB/session.py & PostgreSQL/connect_db.py
"""
#####################################################################################################################################
"""
Formative assignment 2c.2:
"""

products = retrieve_products(connection,["29100","23978","22309"]) #TODO: insert array of products (maybe selected at random?)
print(products)
print(f"The average price of the given products is: €{round((average_price(products)/100), 2)}")
#####################################################################################################################################
"""
Formative assignment 2c.3:
"""
random_product = retrieve_products(connection, [random_product_id(connection)])[0]
print(f"The product with the highest price difference from the random product is {highest_price_difference_product(connection, random_product)}")
#####################################################################################################################################