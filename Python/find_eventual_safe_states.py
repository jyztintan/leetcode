class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        safe = set()
        out_degree = [0] * n
        adj_list = defaultdict(set)

        level = set()
        for node, neighbours in enumerate(graph):
            if len(neighbours) == 0:
                level.add(node)
            else:
                out_degree[node] = len(neighbours)

            for neighbour in neighbours:
                adj_list[neighbour].add(node)

        while level:
            safe.update(level)
            next_level = set()
            for node in level:
                for neighbour in adj_list[node]:
                    out_degree[neighbour] -= 1
                    if out_degree[neighbour] == 0:
                        next_level.add(neighbour)
            level = next_level

        return sorted(list(safe))
