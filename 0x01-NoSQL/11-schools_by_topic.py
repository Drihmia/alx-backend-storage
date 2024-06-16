#!/usr/bin/env python3
""" A module that contains schools_by_topic as a function"""


def schools_by_topic(mongo_collection, topic):
    """
    A function that returns the list of school having a specific topic:

    Arguments:
        mongo_collection: is a pymongo collection object
        topic (string): is the topic searched
    """
    # return mongo_collection.find({"topics": {"$in": [topic]}})
    return mongo_collection.find({"topics": topic})
