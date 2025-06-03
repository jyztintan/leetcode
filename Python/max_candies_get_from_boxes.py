class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]],
                   initialBoxes: List[int]) -> int:
        can_open = initialBoxes
        locked = set()
        visited = set()
        collected = 0
        while can_open:
            box = can_open.pop()
            if box in visited:
                continue
            elif status[box] == 0:
                locked.add(box)
                continue
            collected += candies[box]
            visited.add(box)
            for key in keys[box]:
                status[key] = 1
                if key in locked:
                    can_open.append(key)
                    locked.remove(key)
            for nxt in containedBoxes[box]:
                if status[nxt]:
                    can_open.append(nxt)
                else:
                    locked.add(nxt)
        return collected

