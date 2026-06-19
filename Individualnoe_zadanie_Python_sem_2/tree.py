class Tree:
    def __init__(self):
        self.neighbors = {}
        self.letters = {}

    def add_node(self, node_id, letters_count, neighbors_list):
        self.letters[node_id] = letters_count
        self.neighbors[node_id] = neighbors_list

    def min_apologies(self):
        visited = set()
        apologies = 0

        def dfs(v, parent):
            nonlocal apologies
            visited.add(v)
            children_with_mail = 0
            for to in self.neighbors[v]:
                if to != parent:
                    if dfs(to, v):
                        children_with_mail += 1
            if self.letters[v] > 0:
                if children_with_mail > 1:
                    apologies += children_with_mail - 1
                return True
            else:
                if children_with_mail > 0:
                    apologies += children_with_mail
                    return True
                return False

        dfs(1, -1)
        return apologies