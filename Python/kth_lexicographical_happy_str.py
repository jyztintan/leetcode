# Big brain combinatorics solution that uses math! to avoid even generating non-relevant words
# O(N) since we iterate over the n characters and determine each of them in O(1) time
class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        total = 3 * 2 ** (n - 1)
        if k > total:
            return ""

        next_smallest = {"a": "b", "b": "a", "c": "a"}
        next_greatest = {"a": "c", "b": "c", "c": "b"}

        start_a = 1
        start_b = start_a + (2 ** (n - 1))
        start_c = start_b + (2 ** (n - 1))

        result = ["a"] * n
        if k < start_b:
            result[0] = "a"
            k -= start_a
        elif k < start_c:
            result[0] = "b"
            k -= start_b
        else:
            result[0] = "c"
            k -= start_c

        for char_index in range(1, n):
            midpoint = 2 ** (n - char_index - 1)

            if k < midpoint:
                result[char_index] = next_smallest[result[char_index - 1]]
            else:
                result[char_index] = next_greatest[result[char_index - 1]]
                k -= midpoint

        return "".join(result)


# Stack solution which allows for some short-circuiting when obtaining the kth answer
# However, still same time complexity: O(2^N) because of worst-case
class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        alphabet = "cba"
        st = [""]
        count = 0
        while st:
            word = st.pop()
            if len(word) == n:
                count += 1
                if count == k:
                    return word
                continue

            for letter in alphabet:
                if not word or word[-1] != letter:
                    st.append(word + letter)
        return ""

# Brute force solution: 2^N
class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        alphabet = "abc"
        curr = ["a", "b", "c"]
        for length in range(1, n):
            new_curr = []
            for word in curr:
                for letter in alphabet:
                    if word[-1] == letter:
                        continue
                    new_curr.append(word + letter)
            curr = new_curr

        # k is 1-indexed
        if k > len(curr):
            return ""
        return curr[k - 1]
