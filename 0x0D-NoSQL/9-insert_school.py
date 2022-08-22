#!/usr/bin/env python3
""" Write a Python function that inserts a new document in a collection based on kwargs """
import pymongo


def insert_school(mongo_collection, **kwargs):
    """ inserts a new document """
    new_school = mongo_collection.insert_one(kwargs)
    return (new_school.inserted_id)