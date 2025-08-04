class Edge:
    def __init__(self, target, weight):
        # target is the Vertex object this edge points to
        self.target = target
        self.weight = weight  # weight of the edge (e.g. cost, distance, etc.)


class Vertex:
    def __init__(self, label):
        # label is the name of the vertex (like "A", "B", etc.)
        self.label = label
        self.edges = []  # list to hold all outgoing edges

    def add_edge(self, target, weight):
        # ceate an Edge object that goes to the target vertex with given weight
        edge = Edge(target, weight)
        self.edges.append(edge)  # add the edge to this vertex's edge list

    def remove_edge(self, target):
        # create a new list for edges we want to keep
        edges_copy = []
        for e in self.edges:
            # if this edge does NOT point to the target vertex, append it to the new list (edges_copy)
            if e.target != target:
                edges_copy.append(e)
        # replace old edges list with the filtered one
        self.edges = edges_copy

class Graph:
    def __init__(self):
        # the graph is just a list of Vertex objects
        self.vertices = []

    def add_vertex(self, label):
        # loop through the list of vertices
        for v in self.vertices: 
            if v.label == label: # check if a vertex with this label already exists
                print("error")  # notify the user that the label already exists
                return
        # if not found, create and add a new vertex
        self.vertices.append(Vertex(label))

    def find_vertex(self, label):
        # loop through all vertices to find one with the matching label
        for v in self.vertices:
            if v.label == label:
                return v  # found
        print("not found")
        return None  # not found

    def add_edge(self, label, target, weight):
        # find both vertices by their labels
        vertex1 = self.find_vertex(label)
        vertex2 = self.find_vertex(target)
        # if both vertices exist, create an edge from vertex1 to vertex2 by calling the add_edge method
        if vertex1 is not None and vertex2 is not None: 
            vertex1.add_edge(vertex2, weight)

    def remove_vertex(self, label):
        # first, find the actual vertex object to be removed by calling the find_vertex
        target_vertex = self.find_vertex(label) 
        if not target_vertex:
            return  # nothing to remove

        # for every vertex in the vertices list, remove edges pointing to the target
        for v in self.vertices:
            v.remove_edge(target_vertex)

        # finally, remove the vertex from the graph's list by keeping all the vertices EXCEPT the one that needs to be deleted
        self.vertices = [v for v in self.vertices if v.label != label]

# test run
g = Graph()

# add vertices
g.add_vertex("A")
g.add_vertex("B")

# add an edge A → B with weight 10
g.add_edge("A", "B", 10)

# print A's edges
a = g.find_vertex("A")
for edge in a.edges:
    print(f"A → {edge.target.label} (weight: {edge.weight})")

# remove vertex B
g.remove_vertex("B")

# print A's edges again
print("After removing B:")
for edge in a.edges:
    print(f"A → {edge.target.label} (weight: {edge.weight})")
