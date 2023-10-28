from typing import List


def search_lower(list_of_items: List[int]) -> int:
    lower_item_index = 0
    lower_item = list_of_items[0]

    for index in range(1, len(list_of_items)):
        if list_of_items[index] < lower_item:
            lower_item = list_of_items[index]
            lower_item_index = index

    return lower_item_index


def sort_selection(list_of_items: List[int]) -> List[int]:
    sorted_list = []

    for _ in range(len(list_of_items)):
        lower_item_index = search_lower(list_of_items)
        sorted_list.append(list_of_items.pop(lower_item_index))

    return sorted_list


assert sort_selection([5, 3, 6, 2, 10]) == [2, 3, 5, 6, 10]
assert sort_selection([6, 2, 1, 3, 5, 10]) == [1, 2, 3, 5, 6, 10]
assert sort_selection([1, 1, 1, 1, 10, 10, 2, 2, 5]) == [1, 1, 1, 1, 2, 2, 5, 10, 10]
