INFINIT = float("inf")
GRAPH = {
    "start": {
        "a": 6,
        "b": 2,
    },
    "a": {
        "end": 1,
    },
    "b": {
        "a": 3,
        "end": 5,
    },
    "end": {},
}


def lowest_cost_to_end(graph: dict) -> int:
    processeds = []
    costs = {
        "a": 6,
        "b": 2,
        "end": INFINIT,
    }

    parent = {
        "a": "start",
        "b": "start",
        "end": None,
    }

    node = find_lowest_cost_node(costs, processeds)
    while node:
        node_cost = costs[node]
        neighboors = graph[node]

        for k in neighboors.keys():

            new_cost = node_cost + neighboors[k]

            if costs[k] > new_cost:
                costs[k] = new_cost
                parent[k] = node

        processeds.append(node)
        node = find_lowest_cost_node(costs, processeds)

    return costs["end"]


def find_lowest_cost_node(costs_to_calc: dict, processed: list) -> str:
    lowest_cost = INFINIT
    lowest_cost_node = None

    for node in costs_to_calc:
        cost = costs_to_calc[node]

        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node

    return lowest_cost_node


assert lowest_cost_to_end(GRAPH) == 6
