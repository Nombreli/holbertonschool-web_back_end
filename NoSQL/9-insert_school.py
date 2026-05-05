#!/usr/bin/env python3
"""function that inserts a new document in a collection using kwargs"""


def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document into mongo_collection
    using keyword arguments
    Returns the new document _id
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
