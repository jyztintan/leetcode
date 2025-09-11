class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = 'aeiouAEIOU'
        st = []
        for c in s:
            if c in vowels:
                st.append(c)

        st.sort(reverse=True)
        new = []
        for c in s:
            if c not in vowels:
                new.append(c)
            else:
                new.append(st.pop())
        return "".join(new)
