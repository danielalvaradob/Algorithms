'''
Route Between Nodes: Given a directed graph, 
design an algorithm to find out whether there is a
route between two nodes
 '''


class Node:
    def __init__(self, value):
        self.value = value
        self.visited = False
        self.adjecent_nodes = []
    

class Queue:
    def __init__(self):
        self.elements = []

    def enqueue(self, node):
        # add to queue
        self.elements.append(node)

    def dequeue(self):
        # Remove first element of queue
        element = self.elements[0]
        self.elements.remove(element)
        return element
    
    def is_empty(self):
        return self.elements == []
            



def search(graph, n_start, n_end):
    if (n_end == n_end):
        return True
    
    # queue
    queue = Queue()
    for node in graph:
        node.visited = False
    
    n_start.visited = True
    queue.enqueue(n_start)
    while not queue.is_empty():
        curr_n = queue.dequeue()
        if (curr_n != None):
            for node in curr_n.adjecent_nodes:
                if node.visited == False:
                    if node == n_end: 
                        return True
                    else:
                        queue.enqueue(node)
        curr_n.visited = True
    
    return False
