"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy


class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        self.vertices[v1].add(v2)

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # make a queue
        q = Queue()
        # enqueue our start node
        q.enqueue(starting_vertex)

        # make a set to track visited nodes
        visited = set()

        # while queue still has things in it
        while q.size() > 0:
            # dq from front of the line, this is our current node
            current_node = q.dequeue()
        # check if we've visited, if not:
            if current_node not in visited:
                # mark it as visited
                visited.add(current_node)
                print(current_node)
        # get its neighbors
                neighbors = self.get_neighbors(current_node)
        # iterate over neighbors,
                for neighbor in neighbors:
                    # add to queue
                    q.enqueue(neighbor)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # make a stack
        s = Stack()
        # push our starting node onto the stack
        s.push(starting_vertex)
        # make a set to track the nodes we've visited
        visited = set()

        # as long as our stack isn't empty
        while s.size() > 0:
            # pop off the top, this is our current node
            current_node = s.pop()

        # check if we have visited this before, and if not:
            if current_node not in visited:
                # mark it as visited
                visited.add(current_node)
        # print it (in this case)
                print(current_node)
        # get its neighbors
                neighbors = self.get_neighbors(current_node)
        # iterate over neighbors
                for neighbor in neighbors:
                    # and add them to our stack
                    s.push(neighbor)

    # Base case
    # Progress toward the case
    # Call itself

    def dft_recursive(self, vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        This should be done using recursion.
        """
        if visited == None:
            visited = set()
        # Check if we have been visited
        if vertex not in visited:
            print(vertex)
            visited.add(vertex)
        # Base case: if no neighbors
            neighbors = self.get_neighbors(vertex)
            if len(neighbors) == 0:
                return visited
        # If we do have neighbors, iterate over them and recurse for each one
            for neighbor in neighbors:
                self.dft_recursive(neighbor, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        1. Find the target node
        2. Keep track of how you got there
        """
        # make a queue
        q = Queue()
        # make a set to track visited
        visited = set()
        # enqueue a PATH TO the starting vertex
        path = [starting_vertex]
        q.enqueue(path)
        # as long as our queue isn't empty
        while q.size() > 0:
            # dequeue from the front of the line, this is our current path: []
            current_path = q.dequeue()
        # current_node is the last thing in the current path
            current_node = current_path[-1]
        # check if this is the target node
            if current_node == destination_vertex:
                # if so return
                return current_path
        # check if we've visited yet, if not:
            if current_node not in visited:
                # mark as visited
                visited.add(current_node)
        # get the current node's neighbors
                neighbors = self.get_neighbors(current_node)

        # iterate over the neighbors
                for neighbor in neighbors:
                    # add the neighbor to the path
                    neighbor_path = current_path.copy()
                    neighbor_path.append(neighbor)
        # enqueue the neighbor's path
                    q.enqueue(neighbor_path)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        s = Stack()
        s.push(starting_vertex)
        visited = set()
        while s.size() > 0:
            current = s.pop()
            visited.add(current)
            for edge in self.get_neighbors(current):
                if edge not in visited:
                    s.push(edge)
                if edge is destination_vertex:
                    visited.add(edge)
                    return list(visited)

    # in dfs_recursive, when we hit our base case, we need to return it
    # all the way up

    # when do we want to return from dfs?
    # when we hit the destination vertex!

    def dfs_recursive(self, vertex, destination_vertex, path=[], visited=set()):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
​
        This should be done using recursion.
        """
        # mark our node as visited
        visited.add(vertex)
        # check if it's our target node, if so return
        if vertex == destination_vertex:
            return path
        if len(path) == 0:
            path.append(vertex)
        # iterate over neighbors
        neighbors = self.get_neighbors(vertex)
        # check if visited
        for neighbor in neighbors:
            if neighbor not in visited:
                # if not, recurse with a path
                result = self.dfs_recursive(
                    neighbor, destination_vertex, path + [neighbor], visited)
                # if this recursion returns a path,
                if result is not None:
                    # return from here
                    return result


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
    # graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    # graph.dft(1)
    # graph.dft_recursive(1)

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
    print(graph.dfs_recursive(1, 6))
