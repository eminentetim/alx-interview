#!/usr/bin/python3

def canUnlockAll(boxes):
    if not isinstance(boxes, list):
        return False  # Ensures that the input is a list of lists
    n = len(boxes)  # Total number of boxes
    unlocked = [False] * n  # List to track which boxes are unlocked
    unlocked[0] = True  # The first box is unlocked
    keys = set(boxes[0])  # Start with keys from the first box
    opened = {0}  # Set to track opened boxes
    # Process the keys to open more boxes
    while keys:
        key = keys.pop()  # Get a key
        if key < n and not unlocked[key]:  # If the key can open a new box
            unlocked[key] = True  # Unlock the corresponding box
            opened.add(key)  # Add to the opened boxes
            keys.update(boxes[key])  # Add the new box's keys to the collection
    # If all boxes are unlocked, return True; otherwise, return False
    return all(unlocked)
