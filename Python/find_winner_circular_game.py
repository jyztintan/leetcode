# This is also known as the Josephus Problem
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        # Keep list of alive players
        players = list(range(1, n + 1))
        pointer = 0

        # Game continues while there are at least 2 players
        while len(players) > 1:
            # Get next loser
            pointer = (pointer + k - 1) % len(players)
            # Remove loser
            players.pop(pointer)

        # Output last player standing
        return players[0]
