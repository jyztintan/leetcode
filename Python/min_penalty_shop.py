class Solution:
    def bestClosingTime(self, customers: str) -> int:
        open_penalty = 0 # penalise for being open when no customers
        close_penalty = customers.count('Y') # penalist for being closed when got customer
        best = [close_penalty, 0]
        for idx, c in enumerate(customers):
            if c == 'Y':
                close_penalty -= 1
            else:
                open_penalty += 1
            if close_penalty + open_penalty < best[0]:
                best = [close_penalty + open_penalty, idx + 1]
        return best[1]
