class Solution:
    def lemonadeChange(self, bills) -> bool:
        # Representing $5 and $10 bills
        change = [0, 0]
        for bill in bills:
            if bill == 5:
                change[0] += 1
            elif bill == 10:
                if not change[0]:
                    return False
                change[0] -= 1
                change[1] += 1
            elif bill == 20:
                if change[0] and change[1]:
                    change[0] -= 1
                    change[1] -= 1
                    continue
                if change[0] >= 3:
                    change[0] -= 3
                    continue
                return False
        return True

bills = [5,5,5,10,20]
print(Solution().lemonadeChange(bills))

