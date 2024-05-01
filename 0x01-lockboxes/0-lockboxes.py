#!/usr/bin/python3


def canUnlockAll(boxes):
  """
  This function determines if all boxes can be unlocked using the keys provided.

  Args:
      boxes: A list of lists, where each sublist represents the keys that can open a specific box.

  Returns:
      True if all boxes can be unlocked, False otherwise.
  """

  n = len(boxes)
  unlocked = set([0])  # Track unlocked boxes using a set for faster membership checks
  keys = set(boxes[0])  # Start with keys from the first box

  # Process keys until all boxes are unlocked or no more keys are available
  while keys and len(unlocked) != n:
    new_keys = set()
    for key in keys:
      if key < n and key not in unlocked:
        unlocked.add(key)
        new_keys.update(boxes[key])
    keys = new_keys

  return len(unlocked) == n
