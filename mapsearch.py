"""
Map Search
"""

import comp140_module7 as maps

class Queue:
    """
    A simple implementation of a FIFO queue.
    """
    def __init__(self):
        """
        Initialize the queue.
        """
        self._queue = []

    def __len__(self):
        """
        Returns: an integer representing the number of items in the queue.
        """
        return len(self._queue)

    def __str__(self):
        """
        Returns: a string representation of the queue.
        """
        return str(self._queue)

    def push(self, item):
        """
        Add item to the queue.

        input:
            - item: any data type that's valid in a list
        """
        (self._queue).append(item)

    def pop(self):
        """
        Remove the least recently added item.

        Assumes that there is at least one element in the queue.  It
        is an error if there is not.  You do not need to check for
        this condition.

        Returns: the least recently added item.
        """
        return (self._queue).pop(0)

    def clear(self):
        """
        Remove all items from the queue.
        """
        self._queue = []


class Stack:
    """
    A simple implementation of a LIFO stack.
    """ 
    def __init__(self):
        """
        Initialize the stack.
        """
        self._stack = []

    def __len__(self):
        """
        Returns: an integer representing the number of items in the stack.        
        """
        return len(self._stack)

    def __str__(self):
        """
        Returns: a string representation of the stack.
        """
        return str(self._stack)

    def push(self, item):
        """
        Add item to the stack.

        input:
            - item: any data type that's valid in a list
        """
        (self._stack).append(item)

    def pop(self):
        """
        Remove the most recently added item.

        Assumes that there is at least one element in the stack.  It
        is an error if there is not.  You do not need to check for
        this condition.

        Returns: the most recently added item.
        """
        return (self._stack).pop()

    def clear(self):
        """
        Remove all items from the stack.
        """
        self._stack = []


def bfs_dfs(graph, rac_class, start_node, end_node):
    """
    Performs a breadth-first search or a depth-first search on graph
    starting at the start_node.  The rac_class should either be a
    Queue class or a Stack class to select BFS or DFS.

    Completes when end_node is found or entire graph has been
    searched.

    inputs:
        - graph: a directed Graph object representing a street map
        - rac_class: a restricted access container (Queue or Stack) class to
          use for the search
        - start_node: a node in graph representing the start
        - end_node: a node in graph representing the end

    Returns: a dictionary associating each visited node with its parent
    node.
    """
    dist = {}
    parent = {}
#Initialize all nodes as keys in "dist" and "parent" with default values
    for node in graph.nodes():
        dist[node] = float("inf")
        parent[node] = None
    dist[start_node] = 0
    if rac_class == Queue:
        container = Queue()
    else:
        container = Stack()
    container.push(start_node)
#Iterate through nodes in "container" and 
#setting their actual values in "dist" and "parent"
    while len(container) > 0:
        node = container.pop()
        for neighbor in graph.get_neighbors(node):
            if dist[neighbor] == float("inf"):
                dist[neighbor] = dist[node] + 1
                parent[neighbor] = node
                container.push(neighbor)
                if neighbor == end_node:
                    return parent
    return parent


def dfs(graph, start_node, end_node, parent):
    """
    Performs a recursive depth-first search on graph starting at the
    start_node.

    Completes when end_node is found or entire graph has been
    searched.

    inputs:
        - graph: a directed Graph object representing a street map
        - start_node: a node in graph representing the start
        - end_node: a node in graph representing the end
        - parent: a dictionary that initially has one entry associating
                  the original start_node with None

    Modifies the input parent dictionary to associate each visited node
    with its parent node
    """
    for nbr in graph.get_neighbors(start_node):
        if nbr not in parent.keys():
            parent[nbr] = start_node
            #Perform depth first search recursively on the neighbors of
            #start_node until end_node is found, then return updated parent
            if nbr == end_node:
                return parent
            else:
                dfs(graph, nbr, end_node, parent)
    return parent

def astar(graph, start_node, end_node,
          edge_distance, straight_line_distance):
    """
    Performs an A* search on graph starting at start_node.

    Completes when end_node is found or entire graph has been
    searched.

    inputs:
        - graph: a directed Graph object representing a street map
        - start_node: a node in graph representing the start
        - end_node: a node in graph representing the end
        - edge_distance: a function which takes two nodes and a graph
                         and returns the actual distance between two
                         neighboring nodes
        - straight_line_distance: a function which takes two nodes and
                         a graph and returns the straight line distance 
                         between two nodes

    Returns: a dictionary associating each visited node with its parent
    node.
    """
    #Initialize values for start_node in parent, gcost, hcost, fcost
    #and openset and closedset
    parent = {start_node:None}
    gcost = {start_node:0}
    hcost = {start_node:straight_line_distance(start_node, end_node, graph)}
    fcost = {start_node:gcost[start_node] + hcost[start_node]}
    openset = {start_node:fcost[start_node]}
    closedset = []
    
    while len(openset) > 0:
        #Find the node with the minimum f cost, remove it from openset
        #and place it in closedset
        min_cost = float("inf")
        min_node = None
        for node in openset:
            if openset[node] < min_cost:
                min_cost = openset[node]
                min_node = node
        openset.pop(min_node)
        closedset.append(min_node)
        
        if min_node == end_node:
            return parent
        else:
            for neighbor in graph.get_neighbors(min_node):
                #If neighbor is in open set, check if a shorter actual path has been
                #found and if yes, update gcost, fcost, parent of neighbor
                if neighbor in openset:
                    g_old = gcost[neighbor]
                    g_new = gcost[min_node] + edge_distance(min_node, neighbor, graph)
                    if g_new < g_old:
                        gcost[neighbor] = g_new
                        fcost[neighbor] = g_new + hcost[neighbor]
                        parent[neighbor] = min_node
                        openset[neighbor] = fcost[neighbor]
                #If neighbor is in neither openset nor closedset, initialize its
                #values in gcost, hcost, fcost, parent
                elif neighbor not in closedset:
                    gcost[neighbor] = gcost[min_node] + edge_distance(min_node, neighbor, graph)
                    hcost[neighbor] = straight_line_distance(neighbor, end_node, graph)
                    fcost[neighbor] = gcost[neighbor] + hcost[neighbor]
                    parent[neighbor] = min_node
                    openset[neighbor] = fcost[neighbor]
    return parent

# You can replace functions/classes you have not yet implemented with
# None in the call to "maps.start" below and the other elements will
# work.

maps.start(bfs_dfs, Queue, Stack, dfs, astar)
