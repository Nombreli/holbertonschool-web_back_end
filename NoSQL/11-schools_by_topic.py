#!/usr/bin/env python3
"""function that returns schools having a specific topic"""


def schools_by_topic(mongo_collection, topic):
    """
    Returns list of schools that contain a specific topic
    """
    return list(mongo_collection.find({"topics": topic}))
