class TimeMap:

    def __init__(self):
        self.d = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        # We store the possible values, together with their timestamp in a list
        # We can guarantee that the list is sorted because timestamp is strictly increasing
        if key not in self.d:
            self.d[key] = []

        # Append the timestamp and value for easy binary searching later
        self.d[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:

        # Default is empty string, even if there is no possible answer
        ans = ""

        # Get the possible values of the input key. If the key does not exist then return empty list
        values = self.d.get(key, [])

        # Perform binary search on the timestamps to find the most appropriate [timestamp, value] pair
        low = 0
        high = len(values) - 1
        while low <= high:
            mid = (low + high) // 2

            # If mid timestamp is greater than timestamp then we have exceeded the limit so decrease range
            if values[mid][0] > timestamp:
                high = mid - 1

            # If mid timestamp is less than timestamp then we try to get a pair with a higher timestamp
            elif values[mid][0] < timestamp:

                # Keep track of the best valid answer so far which is this value in the [timestamp, value] pair
                ans = values[mid][1]
                low = mid + 1

            # If the mid pair has the exact timestamp, then we have found the perfect timestamp already
            else:
                ans = values[mid][1]
                break

        return ans


# obj = TimeMap()
# obj.set("foo", "bar", 1)
# print(obj.get("foo", 1))
# print(obj.get("foo", 3))
# obj.set("foo", "bar2", 4)
# print(obj.get("foo", 4))
# print(obj.get("foo", 5))
# print(obj.get("foo", 3))
