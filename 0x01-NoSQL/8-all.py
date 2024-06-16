#!/usr/bin/env python3
"""This module contains list_all as function"""


def list_all(mongo_collection):
    """
    A function that lists all documents in a mongo_collection

    Returns a list of all documents or an emtpy list if no documents
        in the mongo_collection
    """
    return mongo_collection.find()
