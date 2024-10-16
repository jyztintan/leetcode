class FirstUnique:

    def __init__(self, nums):
        self.unique = set()
        self.duplicates = set()
        self.ordered_lst = []
        for num in nums:
            self.add(num)

    def showFirstUnique(self) -> int:
        if not self.unique:
            return -1
        for num in self.ordered_lst:
            if num in self.unique:
                return num

    def add(self, value: int) -> None:
        if value in self.unique:
            self.unique.remove(value)
            self.duplicates.add(value)
        elif value in self.duplicates:
            return
        else:
            self.unique.add(value)
            self.ordered_lst.append(value)


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)