class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        capacity.sort(reverse=True)
        apple = sum(apple)
        packed = 0
        for box, size in enumerate(capacity):
            packed += size
            if packed >= apple:
                return box + 1
