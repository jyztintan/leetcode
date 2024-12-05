from collections import defaultdict


class TimeMap:

    def __init__(self):
        self.d = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.d[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        possible = self.d[key]
        left, right = 0, len(possible) - 1
        ans = -1
        while left <= right:
            mid = (left + right) // 2
            if possible[mid][0] > timestamp:
                right = mid - 1
            else:
                ans = mid
                left = mid + 1
        if ans == -1:
            return ""
        return possible[ans][1]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)


# obj = TimeMap()
# obj.set("foo", "bar", 1)
# print(obj.get("foo", 1))
# print(obj.get("foo", 3))
# obj.set("foo", "bar2", 4)
# print(obj.get("foo", 4))
# print(obj.get("foo", 5))
# print(obj.get("foo", 3))
