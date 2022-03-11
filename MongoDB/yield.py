import session as ses

def get_product_information(product, labels):
    """Get array of infromation from given product, based on labels"""
    prodcuct_info = []
    for label in labels:
        if isinstance(label, list):
            if len(label) == 2:
                try:
                    prodcuct_info.append(product[label[0]][label[1]])
                except KeyError:
                    prodcuct_info.append(None)
            elif len(label) == 3:
                try:
                    prodcuct_info.append(product[label[0]][label[1]][label[2]])
                except KeyError:
                    prodcuct_info.append(None)
        else:
            try:
                prodcuct_info.append(product[label])
            except KeyError:
                prodcuct_info.append(None)
    return prodcuct_info

def get_collection_information(collection, labels):
    """Get array of information from collection, based on given list of labels"""
    collection_info = []
    for item in collection.find():
        collection_info.append(get_product_information(item, labels))
    return collection_info


collection = ses.get_collection(ses.get_database(ses.get_client(), "opisop"), "products")
print(get_collection_information(collection, ["_id", "name", ["price", "selling_price"]]))
