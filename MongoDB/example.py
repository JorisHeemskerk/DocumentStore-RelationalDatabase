import session as ses

def first_product(collection):
    """Return first instance of collection"""
    return collection.find_one()

collection = ses.getCollection(ses.getDatabase(ses.getClient(), "Dataset"), "Products")
print(first_product(collection))