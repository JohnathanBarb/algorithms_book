from typing import List


def sum_recursive(items_to_sum: List[int]) -> int:
    if not items_to_sum:
        return 0

    return items_to_sum[0] + sum_recursive(items_to_sum[1:])


assert sum_recursive([1, 2, 3]) == 6
assert sum_recursive([1, 1, 1, 1, 1, 1, 1, 1, 1]) == 9
