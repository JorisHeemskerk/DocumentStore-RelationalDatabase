import session as ses

def first_product(collection):
    """Return first instance of collection"""
    return collection.find_one()

collection = ses.get_collection(ses.get_database(ses.get_client(), "opisop"), "products")
print(first_product(collection))
