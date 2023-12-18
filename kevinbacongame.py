"""
The Kevin Bacon Game.
"""

import simpleplot
import comp140_module4 as movies

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


def bfs(graph, start_node):
    """
    Performs a breadth-first search on graph starting at the
    start_node.

    inputs:
        - graph: a graph object
        - start_node: a node in graph representing the start node

    Returns: a two-element tuple containing a dictionary
    associating each visited node with the order in which it
    was visited and a dictionary associating each visited node
    with its parent node.
    """
    dist = {}
    parent = {}
#Initialize all nodes as keys in "dist" and "parent" with default values
    for node in graph.nodes():
        dist[node] = float("inf")
        parent[node] = None
    dist[start_node] = 0
    queue = Queue()
    queue.push(start_node)
#Iterate through nodes in "queue" and 
#setting their actual values in "dist" and "parent"
    while len(queue) > 0:
        node = queue.pop()
        for neighbor in graph.get_neighbors(node):
            if dist[neighbor] == float("inf"):
                dist[neighbor] = dist[node] + 1
                parent[neighbor] = node
                queue.push(neighbor)
    return (dist, parent)


def distance_histogram(graph, node):
    """
    Computes the distance between the given node and all other
    nodes in that graph and creates a histogram of those distances.

    inputs:
        - graph: a graph object
        - node: a node in graph

    returns: a dictionary mapping each distance with the number of
    nodes that are that distance from node.
    """
    histogram = {}
    dist = (bfs(graph, node))[0]
#Setting the value of each distance in "dist" to
#the number of nodes of that distance from starting node
    for a_node in dist:
        if dist[a_node] not in histogram:
            histogram[dist[a_node]] = 1
        else:
            histogram[dist[a_node]] += 1
    return histogram


def find_path(graph, start_person, end_person, parents):
    """
    Computes the path from start_person to end_person in the graph.

    inputs:
        - graph: a graph oject with edges representing the connections between people
        - start_person: a node in graph representing the starting node
        - end_person: a node in graph representing the ending node
        - parents: a dictionary representing the parents in the graph

    returns a list of tuples of the path in the form:
        [(actor1, {movie1a, ...}), (actor2, {movie2a, ...}), ...]
    """
    path = []
    parent = parents[end_person]
    path_key = [parent,end_person]
#Checking conditions if start_person and end_person are the same, 
#and if end_person does not have a parent
    if start_person == end_person:
        return [(end_person,set())]
    if parent == None:
        return []
#Append actors to "path_key" in the order from start_person to end_person
    while parent != start_person:
        parent = parents[parent]
        path_key.insert(0, parent)
#Append tuples consisting of actor and shared movies to "path"
    for idx in range(len(path_key)-1):        
        path.append((path_key[idx],graph.get_attrs(path_key[idx], path_key[idx+1])))
    path.append((end_person,set()))
    return path

def play_kevin_bacon_game(graph, start_person, end_people):
    """
    Play the "Kevin Bacon Game" on the actors in the given
    graph.

    inputs:
        - graph: a graph object with edges representing the connections between people
        - start_person: a node in graph representing the node from which the search will start
        - end_people: a list of nodes in graph to which the search will be performed

    Prints the results out.
    """
    for end_person in end_people:
        movies.print_path(find_path(graph, start_person, end_person, (bfs(graph, start_person))[1]))

def run():
    """
    Load a graph and play the Kevin Bacon Game.
    """
    graph5000 = movies.load_graph('subgraph5000')

    if len(graph5000.nodes()) > 0:
        # You can/should use smaller graphs and other actors while
        # developing and testing your code.
        play_kevin_bacon_game(graph5000, 'Kevin Bacon',
            ['Amy Adams', 'Andrew Garfield', 'Anne Hathaway', 'Barack Obama', \
             'Benedict Cumberbatch', 'Chris Pine', 'Daniel Radcliffe', \
             'Jennifer Aniston', 'Joseph Gordon-Levitt', 'Morgan Freeman', \
             'Sandra Bullock', 'Tina Fey'])

        # Plot distance histograms
        for person in ['Kevin Bacon', 'Stephanie Fratus']:
            hist = distance_histogram(graph5000, person)
            simpleplot.plot_bars(person, 400, 300, 'Distance', \
                'Frequency', [hist], ["distance frequency"])

# Uncomment the call to run below when you have completed your code.

run()
