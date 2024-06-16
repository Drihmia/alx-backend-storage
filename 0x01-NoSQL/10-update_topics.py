#!/usr/bin/env python3
""" A module that contains a function called : update_topics"""


def update_topics(mongo_collection, name, topics):
    """
    A function that changes all topics of a school document based on the name:

    Arguments:
        mongo_collection: is  a pymongo collection object
        name (string): is a school name to update
        topics (str's list): is a list of topics approached in the school
    """
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
