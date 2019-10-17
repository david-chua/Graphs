def bft(start_node):
#make a queue, so the nodes we are about ot visit can wait in line
q = Queue()
# make a set, to track all the nodes we have already visited
visited = set()
#enqueue the start node
q.enqueue(start_node)
# while this queue isn't empty:
while q.length():
##dequeue whatever is at the front, and this is our current node
    current_node = q.dequeue()
## if current node has not yet been visited:
    if current_node not in visited:
## mark the current node as visited by putting it in our visited set
        visited.add(current_node)
## get all of the current node's friends/ neighbors
        neighbors = getNeighbors()
## for each of those friends:
        for neighbor in neighbors:
## put them in our queue to be visited.
            q.enqueue(neighbor)
#
# q = =Queue()
# visited = set()
#
# current_node =

def dft(start_node):
    # make a stack, for the nodes we are about to visit
    # make a set for visited nodes
    # put hte start node on the stack
    # while this stack isn't empty:

    # pop off whatever is on top of the stack, this is our current node
    ## if current node has not yet been visited:
    ### mark the current node as visited by putting it in our visited set
    ### get all of the current node's friends/ neighbors
            ## for each of those friends:
            ## put them in our stack to be visited

s = Stack(G, F, C)

visited = set(A, B, D)

current_node = D

neighbords[F, G]
