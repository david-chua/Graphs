"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
    def add_vertex(self, vertex):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        set_of_friends = self.vertices[v1]
        set_of_friends.add(v2)

    def getNeighbors(self, vertex):
        return self.vertices[vertex]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        #make a queue so the nodes we are about to visit can wait in line
        q = Queue()
        # make a set to track all the nodes we have already visited
        visited = set()

        #enqueue the start node
        q.enqueue(starting_vertex)
        ## while this queue isn't empty:
        while q.size():
            # dequeue whatever is at the front, and this is our current node
            current_node = q.dequeue()
            # if current node has not yet been visited:
            if current_node not in visited:
                #makr the current node as visited by putting it in the visited set
                visited.add(current_node)
                print(current_node)

                #get all of the current node's friends/ neighbors
                neighbors = self.getNeighbors(current_node)
                print('current node neighbors', neighbors)

                ## for each of those friends:
                for neighbor in neighbors:
                    ## put them into our queue to be visited
                    q.enqueue(neighbor)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        #make a stack, for those nodes we are about to visit
        stack = Stack()
        # make a set for visited nodes
        visited = set()
        # put the start node on the stack
        stack.push(starting_vertex)
        # while the stack isn't empty:
        while stack.size():
            ## pop off whatever is on top of the stack, this is our current node
            current_node = stack.pop()
            print(current_node)
            ## if current node has not yet been visited:
            if current_node not in visited:
                visited.add(current_node)
                neighbors = self.getNeighbors(current_node)
                for neighbor in neighbors:
                    stack.push(neighbor)

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


    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        if starting_vertex not in self.vertices or destination_vertex not in self.vertices:
            return "Vertex not found"
        visited = set()
        stack = Stack()
        stack.push(starting_vertex)
        while stack.size():
            current_vertex = stack.pop()
            if current_vertex not in visited:
                visited.add(current_vertex)
                if current_vertex == destination_vertex:
                    return visited
                neighbors = self.getNeighbors(current_vertex)
                if neighbors and len(neighbors):
                    for neighbor in neighbors:
                        stack.push(neighbor)






if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT recursive paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
