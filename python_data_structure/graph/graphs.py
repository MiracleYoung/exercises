class Vertex:
    def __init__(self, key):
        self._id = key
        self._connected_to = {}

    def add_neighbor(self, nbr, weight=0):
        self._connected_to[nbr] = weight

    def __str__(self):
        return str(self._id) + ' connected to :' + str([x._id for x in self._connected_to])

    def get_connections(self):
        return self._connected_to.keys()

    def get_id(self):
        return self._id

    def get_weight(self, nbr):
        return self._connected_to[nbr]

    def get_color(self):
        pass

    def set_color(self, color):
        pass

    def get_distance(self):
        pass

    def set_distance(self, distance):
        pass

    def set_pred(self, value):
        pass

    def predecessor(self):
        pass

    def color(self):
        pass


class Graph:
    def __init__(self):
        self._vertex_list = {}
        self._num_vertex = 0

    def add_vertex(self, key):
        self._num_vertex += 1
        _new_vertex = Vertex(key)
        self._vertex_list[key] = _new_vertex
        return _new_vertex

    def get_vertex(self, key):
        return self._vertex_list[key] if key in self._vertex_list else None

    def __contains__(self, item):
        return item in self._vertex_list

    def add_edge(self, f, t, cost=0):
        if f not in self._vertex_list:
            self.add_vertex(f)
        if t not in self._vertex_list:
            self.add_vertex(t)
        self._vertex_list[f].add_neighbor(self._vertex_list[t], cost)

    def get_vertices(self):
        return self._vertex_list.keys()

    def __iter__(self):
        return iter(self._vertex_list.values())


if __name__ == '__main__':
    g = Graph()
    for i in range(6):
        g.add_vertex(i)

    print(g._vertex_list)

    g.add_edge(0, 1, 5)
    g.add_edge(0, 5, 2)
    g.add_edge(1, 2, 4)
    g.add_edge(2, 3, 9)
    g.add_edge(3, 4, 7)
    g.add_edge(3, 5, 3)
    g.add_edge(4, 0, 1)
    g.add_edge(5, 4, 8)
    g.add_edge(5, 2, 1)

    for v in g:
        for w in v.get_connections():
            print("( %s , %s )" % (v.get_id(), w.get_id()))
