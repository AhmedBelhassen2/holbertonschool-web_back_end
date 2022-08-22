#!/usr/bin/env python3
"""Write a Python function that lists all documents in a collection """
import pymongo


def list_all(mongo_collection):
    """ List all elements in a collection """
    return mongo_collection.find() or []
