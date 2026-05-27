class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        lower_seen = set()
        special = set()
        dead = set()
        for c in word:
            if c.islower():
                if c.upper() in special:
                    special.remove(c.upper())
                    dead.add(c.upper())
                lower_seen.add(c)
            else:
                if c.lower() not in lower_seen:
                    dead.add(c)
                if c.lower() in lower_seen and c not in dead:
                    special.add(c)
        return len(special)
