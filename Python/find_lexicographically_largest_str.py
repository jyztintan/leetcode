class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        if numFriends == 1:
            return word

        n = len(word)
        left, right = 0, 1
        while right < n:
            window = 0
            while right + window < n and word[left + window] == word[right + window]:
                window += 1
            if right + window < n and word[left + window] < word[right + window]:
                left, right = right, max(right + 1, left + window + 1)
            else:
                right += window + 1
        last = word[left:]
        return last[: min(len(last), n - numFriends + 1)]
