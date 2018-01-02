# breadth-first search implementation
from collections import deque

# create our mock graph
graph = {}
graph["parker"] = ["bess", "hannah", "liilia"]
graph["bess"] = ["tess", "ella"]
graph["hannah"] = ["olivia", "emma"]
graph["liilia"] = ["andres", "arnav"]
graph["tess"] = []
graph["ella"] = []
graph["olivia"] = []
graph["emma"] = []
graph["andres"] = []
graph["arnav"] = []

"""
mock function for flagging a node as "correct"
the person is a pal.
"""
def person_is_pal(person):
    return person[-1] == "a"

def breadthFirstSearch(name):

    # create our queue
    search_queue = deque()
    search_queue += graph[name]

    # create an empty list to keep track of searched pals
    searched = []

    # iterate through the queue
    while search_queue:

        # deque / pop the first person off the queue
        person = search_queue.popleft()

        """
        check that we haven't already checked this person.
        failing to do this could get us in an infinite loop.
        """

        if not person in searched:
            if person_is_pal(person):
                # search is complete
                print person + " is a pal"
                return True
            else:
                # not a pal, add their neighbors to the search
                search_queue += graph[person]

                # add them to the searched array
                searched.append(person)
    print "No one is a pal :("
    return False

print breadthFirstSearch("parker")
print breadthFirstSearch("bess")
print breadthFirstSearch("hannah")
print breadthFirstSearch("liilia")

# runtime O(V + E) - number of vertices plus number of edges