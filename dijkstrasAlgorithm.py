"""
an implementation of Dijkstra's Algorithm.

Dijkstra's Algorithm is comprised of four parts:

1) Find the "cheapest" node - the node with the smallest
weight.
2) Update the costs of the neighbors of the node.
3) Repeat until you've done this for every node in the graph.
4) Calculate the final path.

Note that Dijkstra's Algorithm only works for directed acycle
graphs (DAGs). Furthermore, it only works when weights applied
to graph edges are non-negative.
"""

# create our graph hash
graph = {}
graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2
graph["a"] = {}
graph["a"]["fin"] = 1
graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["fin"] = 5
graph["fin"] = {}

# create our costs hash
infinity = float("inf")
costs = {}
costs["a"] = 6
costs["b"] = 2
costs["fin"] = infinity

# create our parents hash
parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["fin"] = None

# create an array to store processed nodes
processed = []

# and a path hash to store the path
path = {}

# create a function to find the lowest cost node
def find_lowest_cost_node(costs):

    # variables for storing lowest cost node
    lowest_cost = infinity
    lowest_cost_node = None

    """
    check the cost of each node,
    skipping ones that have been processed
    """
    for node in costs:
        cost = costs[node]

        # if the cost is lower than the lowest
        if cost < lowest_cost and node not in processed:

            # update the cost and node
            lowest_cost = cost
            lowest_cost_node = node
    
    # return the lowest cost node
    return lowest_cost_node

def dijkstrasAlgorithm(graph, costs, parents, processed):
    node = find_lowest_cost_node(costs)
    while node is not None:
        cost = costs[node]
        neighbors = graph[node]
        for n in neighbors.keys():
            new_cost = cost + neighbors[n]
            if costs[n] > new_cost:
                costs[n] = new_cost
                parents[n] = node
                path[n] = node
        processed.append(node)
        node = find_lowest_cost_node(costs)

    return path

print dijkstrasAlgorithm(graph, costs, parents, processed)