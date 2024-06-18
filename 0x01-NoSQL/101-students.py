#!/usr/bin/env python3
""" THis module contains a function called: top_students """


def top_students(mongo_collection):
    """
    A  Python function that returns all students sorted by average score:
    mongo_collection will be the pymongo collection object

    The top must be ordered
    The average score must be part of each item returns with key = averageScore
    """

    first_stage = {
        "$project": {
            "_id": 1,
            "name": 1,
            # "averageScore": {"$divide": [
            # {"$sum": "$topics.score"},
            # {"$size": "$topics"}
            # ]
            # },
            "averageScore": {
                "$cond": {
                    "if": {"$gt": [{"$size": "$topics"}, 0]},
                    "then": {"$divide": [
                        {"$sum": "$topics.score"},
                        {"$size": "$topics"}
                    ]
                             },
                    "else": 0
                }
            }
        }
    }

    sorting_stage = {
        "$sort": {"averageScore": -1}
    }

    pipeline = [first_stage, sorting_stage]
    return mongo_collection.aggregate(pipeline)
