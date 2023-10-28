from typing import List


def max_recursive(items: List[int]) -> int:
    if len(items) == 1:
        return items[0]

    item1 = items[0]
    item_to_consider = max_recursive(items[1:])

    return item1 if item1 >= item_to_consider else item_to_consider


assert max_recursive([1, 2, 3, 4, 5]) == 5
assert max_recursive([10, 11, 50, 1]) == 50

