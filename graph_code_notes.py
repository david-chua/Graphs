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

    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        This should be done using recursion.
        """
        if not self.vertices:
            raise VertexNotFound("Sorry, the vertex doesn't exist")
        result = []
        visited = set()
        def dft(vertex, visited, result):
            if vertex not in visited:
                visited.add(vertex)
                result.append(str(vertex))
                neighbors = self.getNeighbors(vertex)
                if neighbors and len(neighbors) > 0:
                    for neighbor in neighbors:
                        dft(neighbor, visited, result)

        dft(starting_vertex, visited, result)
        print("Recursive DFT: " + " ".join(result))
        return result

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        visited = {}
        queue = Queue()
        visited[starting_vertex] = [starting_vertex]
        queue.enqueue(starting_vertex)
        while queue.size():
            current_vertex=queue.dequeue()
            neighbors = self.getNeighbors(current_vertex)
            for neighbor in neighbors:
                if neighbor not in visited:
                    visited[neighbor] = visited[current_vertex][:]
                    visited[neighbor].append(neighbor)
                    if destination_vertex is not None and neighbor == destination_vertex:
                        return visited[neighbor]
                    queue.enqueue(neighbor)
        return visited



How to solve any graph problems
1) Describe the problem in graph terminalogy

Nodes: words
Edges: one letter differences

2) Build a graph or define our getNeighbors function

build a graph option:

Iteerate over all the words and add_vertex
for every node:
    for every other node:
        check if they are one letter different
        if so, make an edge

open("words.txt", "r")

words = file.read().split('\n')
file.close()

word_set = set()
for word in words:
    word_set.add(word.lower())

alphabet = list(string.ascii_lowercase)

def get Neightbors(word):
    neighbors = []
    # for each letter in the word:
    for letter_index in range(len(word)):
        # for each letter in the alphabet
        for alphabet_letter in alphabet:
            # turn the word into a list
            word_list = list(word)
            #sub the alphabet-letter for the word letter
            word_list[letter_index] = alphabet_letter
            #turn the word list back into a string
            maybe_neighbor = "".join(word_list)
            #CHECK IF THIS NEW WORD IS IN OUR WORD-LIST
            if maybe_neighbor in word_set and maybe_neighbor is not word:
                #if so add to our list of neighbors
                neighbors.append(maybe_neighbor)

    return neighbors

def bfs(start_word, target_word):
    q = Queue()
    visited = set()
    path = [start_word]
    q.enqueue(path)

    while q.size() > 0:
        current_path = q.dequeue()
        current_node = current_path[-1]
        if current_node == target_word:
            return current_path
        if current_node not in visited:
            visited.add(current_node)
            neighbor_words = getNeighbors(current_node)
            for neighbor_word in neighbor_words:
                path_copy = list(current_path)
                path_copy.append(neighbor_word)
                q.enqueue(path_copy)
