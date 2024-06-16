#!/usr/bin/env python3
""" A module that contains a function called : insert_school"""


def insert_school(mongo_collection, **kwargs):
    """
    A function  inserts a new document in a collection based on kwargs

    Return: new _id
    """
    inserted_doc = mongo_collection.insert_one(kwargs)
    return inserted_doc.inserted_id
