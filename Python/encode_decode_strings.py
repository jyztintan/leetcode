# If we are allowed to use non-ascii characters then simply use any as a delimiter
# Time O(N): just need to add/split delimiter between the words
# Space O(N + K): we would get an output of N characters plus K instances for delimiters
# where N and K are the total number of characters and words in strs.
class Codec:
    def encode(self, strs) -> str:
        """Encodes a list of strings to a single string.
        """
        encoded = ''
        for word in strs:
            encoded += word.replace('/', '//') + '/$'
        return encoded

    def decode(self, s: str):
        """Decodes a single string to a list of strings.
        """
        decoded = []
        ptr = 0
        curr = ''
        while ptr < len(s):
            if s[ptr:ptr + 2] == '/$':
                decoded.append(curr)
                curr = ""
                ptr += 2
            elif s[ptr:ptr + 2] == "//":
                curr += '/'
                ptr += 2
            else:
                curr += s[ptr]
                ptr += 1
        return decoded


# If we are allowed to use non-ascii characters then simply use any as a delimiter
# Time O(N): just need to add/split delimiter between the words
# Space O(N + K): we would get an output of N characters plus K instances for delimiters
# where N and K are the total number of characters and words in strs.
class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        return 'π'.join(strs)

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        return s.split('π')


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))