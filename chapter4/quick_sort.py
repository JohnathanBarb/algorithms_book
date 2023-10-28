from typing import List


def quick_sort(numbers: List[int]) -> List[int]:
    if len(numbers) < 2:
        return numbers

    higgers = []
    minors = []
    number_base = numbers[0]

    for number in numbers[1:]:

        if number > number_base:
            higgers.append(number)
            continue

        minors.append(number)

    return quick_sort(minors) + [number_base] + quick_sort(higgers)


assert quick_sort([5, 3, 6, 2, 10]) == [2, 3, 5, 6, 10]
assert quick_sort([6, 2, 1, 3, 5, 10]) == [1, 2, 3, 5, 6, 10]
assert quick_sort([1, 1, 1, 1, 10, 10, 2, 2, 5]) == [1, 1, 1, 1, 2, 2, 5, 10, 10]
