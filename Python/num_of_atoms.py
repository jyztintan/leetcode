class Solution:
    def countOfAtoms(self, formula: str) -> str:

        n = len(formula)
        d = {}
        # To store previous states if we encounter brackets
        st = []
        ptr = 0
        while ptr < n:
            char = formula[ptr]

            # Process new element
            if char.isupper():

                # Getting the whole element string representation
                start = ptr
                ptr += 1
                while ptr < n and formula[ptr].islower():
                    ptr += 1
                element = formula[start:ptr]

                # Getting the whole element numeric representation
                start = ptr
                while ptr < n and formula[ptr].isnumeric():
                    ptr += 1
                # If the count was not specified then the count is 1
                number = int(formula[start:ptr]) if start != ptr else 1
                d[element] = d.get(element, 0) + number

            # If we encounter an opening bracket, we add the current state to the stack
            # and start from a new state as we need to modify the count within the brackets
            elif char == "(":
                st.append(d.copy())
                d = {}
                ptr += 1

            # We close the brackets so now we need to process the count of the elements in the brackets.
            # We find the multiplier and modify the counts of each element in the brackets with the multiplier
            # We add these counts to the previous state that we pop from the stack
            elif char == ")":
                ptr += 1
                start = ptr
                while ptr < n and formula[ptr].isnumeric():
                    ptr += 1
                multiplier = int(formula[start:ptr]) if start != ptr else 1
                prev_d = st.pop()
                for ele, count in d.items():
                    prev_d[ele] = prev_d.get(ele, 0) + multiplier * count
                d = prev_d

        # We want to return the final string representation sorted by elements
        lst = sorted(d.keys())
        ans = ""
        for key in lst:
            # If the count is 1, we don't need to specify the count
            count = str(d[key]) if d[key] > 1 else ""
            ans += str(key) + count
        return ans

# print(Solution().countOfAtoms("Mg20O4H"))
# print(Solution().countOfAtoms("K4(ON(SO3)2)2"))
# print(Solution().countOfAtoms("H2O"))
