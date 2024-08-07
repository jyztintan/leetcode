class Solution:
    def __init__(self):
        self.ones = [0, "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
        self.special = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        self.tens = [0, 1, "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        self.suffix = ["", "Thousand", "Million", "Billion", "Trillion"]
    def numberToWords(self, num: int) -> str:
        # Edge case for zero
        if not num:
            return 'Zero'

        # Helper function for digits of 3s
        def spell(num):
            s = ""
            third = num//100
            second = (num % 100)//10
            first = num % 10
            special = False
            # If there is a hundred, spell out the hundred
            if self.ones[third]:
                s += f"{self.ones[third]} Hundred"
            # If there is a tens place digit, need to check if it is a special case 1
            if self.tens[second]:
                if second == 1:
                    special = True
                else:
                    if s:
                        s += " "
                    s += self.tens[second]
            if self.ones[first] or special:
                if s:
                    s += " "
                # If special case, then tailor the algo appropriately
                if special:
                    s += self.special[first]
                else:
                    s += self.ones[first]
            return s

        ans = ""
        # Helps us keep track of which suffix to use
        multiplier = 0
        while num:
            # We break down the numbers into 3-digits
            part = spell(num % 1000)
            if part:
                if ans:
                    part += " " + self.suffix[multiplier] + " " if self.suffix[multiplier] else " "
                else:
                    part += " " + self.suffix[multiplier] if self.suffix[multiplier] else ""
                ans = part + ans
            num //= 1000
            multiplier += 1

        return ans.strip()
