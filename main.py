#############################################################################################
#                                                                                           #
#   This file will excecute all requested excersises laid out in "Formatieve opdracht 2c"   #
#                                                                                           #
#############################################################################################
import PostgreSQL.connect_db as connect
import random
# random.seed(0)


def retrieve_ids(connection):
    """Retrieve all product ids

    @params
    connection: A connection to the required database

    return: list of all product ids
    """
    cursor = connection.cursor()
    cursor.execute('''SELECT id FROM products;''')
    product_ids = cursor.fetchall()
    cursor.close()
    return product_ids

def random_product_id(connection, product_ids):
    """Retrieve random product id from PostgreSQL database

    @params
    connection: A connection to the required database
    product_ids: A list of all possible product ids

    return: product id of randomly selected product
    """
    return product_ids[random.randint(0, len(product_ids) - 1)][0]

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
    cursor.close()
    return products

def retrieve_price(connection):
    cursor = connection.cursor()
    cursor.execute('''SELECT price FROM products;''')
    product_prices = cursor.fetchall()
    cursor.close()
    product_prices = [p[0] for p in product_prices]
    return product_prices

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

# def highest_price_difference_product(connection, product_id):
#     """find product with highest price difference to given product (corresponding to id)
#
#     @params
#     connection: A connection to the required database
#     product_id: id, refering to a product item from datbase
#
#     return: the first product with the highest price difference to given product
#     """
#     difference = 0
#     highest_difference_product = None
#     all_ids = retrieve_ids(connection)
#     cursor = connection.cursor()
#     cursor.execute(f"SELECT * from products where id = '{product_id}'")
#     product = cursor.fetchall()
#
#     for i, id in enumerate(all_ids):
#         percentage = round(i / (len(all_ids) - 1) * 100, 2)
#         print('Progress: [{}{}{}]  {}%'.format(('=' * int(percentage // 10)), ('>' if percentage < 100 else ''),('.' * int(10 - (((percentage) // 10)) - 1)), percentage))
#         try:
#             cursor.execute(f"SELECT * from products where id = '{id[0]}'")
#             comparative_product = cursor.fetchall()
#             if abs(product[0][2] - comparative_product[0][2]) > difference:
#                 difference = abs(product[0][2] - comparative_product[0][2])
#                 highest_difference_product = comparative_product
#         except:
#             continue
#     cursor.close()
#     return highest_difference_product

def highest_price_difference_product(connection, product_id):
    """
    find product with highest price difference to given product (corresponding to id)
    @params
    connection: A connection to the required database
    product_id: id, refering to a product item from datbase

    return: the first product with the highest price difference to given product
    """
    cursor = connection.cursor()
    cursor.execute(f"SELECT * from products where id = '{product_id}'")
    product = cursor.fetchall()
    product_price = product[0][2]
    prices = retrieve_price(connection)
    not_null_prices = [item for item in prices if item !=None]
    highest = max(not_null_prices)
    lowest = min(not_null_prices)

    cursor.execute('''SELECT * FROM products;''')
    products = cursor.fetchall()
    cursor.close()

    if (highest - product_price) > (product_price - lowest):
        highest_difference_product = highest
    else:
        highest_difference_product = lowest
    highest_difference_product = products[prices.index(highest_difference_product)]

    return highest_difference_product


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
products = retrieve_products(connection, [id[0] for id in retrieve_ids(connection)[20:70]])
print(f"The average price of the given products is: €{round((average_price(products)/100), 2)}")
#####################################################################################################################################
"""
Formative assignment 2c.3:
"""
random_id = random_product_id(connection,retrieve_ids(connection))
#random_id = 44076

cursor = connection.cursor()
cursor.execute(f"SELECT * from products where id = '{random_id}'")
random_product = cursor.fetchall()
cursor.close()

price_difference_highest_product = highest_price_difference_product(connection, random_id)
print(f"The product with the highest price difference from {random_product[0][1]} (with a price of €{round((random_product[0][2]/100), 2)}) is {price_difference_highest_product[1]} (with a price of €{round((price_difference_highest_product[2]/100), 2)})\nThis results in a difference of €{round((abs(price_difference_highest_product[2]-random_product[0][2])/100), 2)}")
#####################################################################################################################################
