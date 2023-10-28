def count_recursive(items_to_count: list) -> int:
    if not items_to_count:
        return 0

    return 1 + count_recursive(items_to_count[1:])


assert count_recursive(list(range(10))) == 10
assert count_recursive(list(range(7))) == 7
assert count_recursive(list(range(99))) == 99

# assert count_recursive(list(range(1000))) == 1000
# recursion error on call 997
