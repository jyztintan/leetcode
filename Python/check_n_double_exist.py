class Solution:
    def checkIfExist(self, arr) -> bool:
        double = set()
        for num in arr:
            if num / 2 or num * 2 in double:
                return True
            double.add(num)
        return False
