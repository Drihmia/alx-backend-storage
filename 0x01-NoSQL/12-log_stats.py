#!/usr/bin/env python3
"""This module contains a function called nginx_logs"""
from pymongo import MongoClient


def nginx_logs(collection):
    """
    A function that provides some stats about Nginx logs stored in mongodb

    Arguments:
        db: database
        collection: collection to read logs from.

    Return: a string as the following example:
        <number_logs> logs
        Methods:
            method GET: <number_get>
            method POST: <number_post>
            method PUT: <number_put>
            method PATCH: <number_patch>
            method DELETE: <number_delete>
        <number_logs_checked> status check

        *number_logs_checked: number of documents with:
                                        method=GET, path=/status.
    """

    # Counting all documents in the collection nginx
    number_logs = collection.count_documents({})

    # Counting documents that has the path as '/status'.
    number_logs_checked = collection.count_documents({"path": "/status"})

    # Counting documents with specific method.
    number_get = collection.count_documents({"method": "GET"})
    number_post = collection.count_documents({"method": "POST"})
    number_put = collection.count_documents({"method": "PUT"})
    number_patch = collection.count_documents({"method": "PATCH"})
    number_delete = collection.count_documents({"method": "DELETE"})

    string = f"""{number_logs} logs
Methods:
\tmethod GET: {number_get}
\tmethod POST: {number_post}
\tmethod PUT: {number_put}
\tmethod PATCH: {number_patch}
\tmethod DELETE: {number_delete}
{number_logs_checked} status check"""

    return string


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx = client.logs.nginx
    print(nginx_logs(nginx))
