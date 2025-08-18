class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        cards = list(map(float, cards))
        EPS = 1e-6

        def backtrack(cards):
            if len(cards) == 1:
                return abs(cards[0] - 24) < EPS

            n = len(cards)
            for i, card1 in enumerate(cards):
                for j in range(i + 1, n):
                    card2 = cards[j]
                    # Put unused cards back
                    new_cards = [cards[k] for k in range(n) if k != i and k != j]
                    next_move = [card1 + card2, card1 * card2, card1 - card2, card2 - card1]
                    if abs(card1) > EPS:
                        next_move.append(card2 / card1)
                    if abs(card2) > EPS:
                        next_move.append(card1 / card2)
                    for move in next_move:
                        new_cards.append(move)
                        if backtrack(new_cards):
                            return True
                        new_cards.pop()
            return False

        return backtrack(cards)
