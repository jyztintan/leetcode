class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        n = len(edges)

        # Find the distances of all nodes from node1 and node2
        def get_distances(node):
            dist = [-1] * n
            curr = node
            count = 0
            while curr != -1 and dist[curr] == -1:
                dist[curr] = count
                count += 1
                curr = edges[curr]
            return dist

        dist1 = get_distances(node1)
        dist2 = get_distances(node2)

        best = [-1, float('inf')]  # node, distance
        for node in range(n):
            if dist1[node] != -1 and dist2[node] != -1:
                max_dist = max(dist1[node], dist2[node])
                if max_dist < best[1]:
                    best = [node, max_dist]
        return best[0]
