def factorial(number: int) -> int:
    if number == 1:
        return number

    return number * factorial(number - 1)


assert factorial(1) == 1
assert factorial(2) == 2
assert factorial(3) == 6
assert factorial(5) == 120
assert factorial(10) == 3628800
