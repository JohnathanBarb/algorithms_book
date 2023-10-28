from typing import Optional, List


def binary_search(list_to_search: List[int], item_to_search: int) -> Optional[int]:

    lowest_index = 0
    highest_index = len(list_to_search) - 1

    while lowest_index <= highest_index:
        middle_index_to_search = (lowest_index + highest_index) // 2
        item_on_middle = list_to_search[middle_index_to_search]

        if item_on_middle == item_to_search:
            return middle_index_to_search

        if item_on_middle > item_to_search:
            highest_index = middle_index_to_search - 1
            continue

        lowest_index = middle_index_to_search + 1

    return None


list_to_test = [1, 3, 5, 7, 9]

assert binary_search(list_to_test, 3) == 1
assert binary_search(list_to_test, -1) is None
