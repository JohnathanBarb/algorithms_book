from collections import deque
from typing import Optional


graph = {
    "me": ["alice", "bob", "claire"],
    "bob": ["anuj", "peggy"],
    "alice": ["peggy"],
    "claire": ["thom", "jonny"],
    "anuj": [],
    "peggy": [],
    "thom": [],
    "jonny": [],
}


def person_has_mango_seller_contact(name_to_start: str, mango_seller_name: str) -> Optional[str]:
    def person_sell_mango(name: str):
        return name == mango_seller_name

    search_deque = deque()
    search_deque += graph[name_to_start]
    searched_persons = []

    while search_deque:
        person = search_deque.popleft()
        if person in searched_persons:
            continue

        if person_sell_mango(person):
            return person

        search_deque += graph[person]
        searched_persons.append(person)

    return


assert person_has_mango_seller_contact("me", "johnathan") is None
assert person_has_mango_seller_contact("me", "thom") == "thom"
assert person_has_mango_seller_contact("me", "anuj") == "anuj"
assert person_has_mango_seller_contact("me", "peggy") == "peggy"
assert person_has_mango_seller_contact("me", "jonny") == "jonny"
assert person_has_mango_seller_contact("me", "claire") == "claire"
assert person_has_mango_seller_contact("me", "bob") == "bob"
assert person_has_mango_seller_contact("me", "alice") == "alice"
assert person_has_mango_seller_contact("me", "joseph") is None
assert person_has_mango_seller_contact("me", "jose") is None
assert person_has_mango_seller_contact("me", "josephine") is None
assert person_has_mango_seller_contact("me", "a") is None
assert person_has_mango_seller_contact("me", "b") is None
