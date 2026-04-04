class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        parent_to_child = defaultdict(list)
        for i, child in enumerate(pid):
            parent = ppid[i]
            parent_to_child[parent].append(child)

        killed = []
        q = [kill]
        while q:
            process = q.pop()
            killed.append(process)
            for child in parent_to_child[process]:
                q.append(child)

        return killed
