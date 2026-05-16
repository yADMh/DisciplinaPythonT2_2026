

class GraphAdjList:
    def __init__(self):
        self.adj = {}

    # Exercício 7
    def add_vertex(self, v):
        if v not in self.adj:
            self.adj[v] = []

    def add_edge(self, u, v, directed=False):
        self.add_vertex(u)
        self.add_vertex(v)

        self.adj[u].append(v)

        if not directed:
            self.adj[v].append(u)

    def print_graph(self):
        for v in self.adj:
            print(v, "->", self.adj[v])

    # Exercício 10
    def to_mermaid(self, directed=False):
        result = "graph TD\n"

        visited = set()

        for u in self.adj:
            for v in self.adj[u]:

                edge = tuple(sorted([u, v]))

                if not directed and edge in visited:
                    continue

                visited.add(edge)

                result += f"    {u} -- {v}\n"

        return result
    

