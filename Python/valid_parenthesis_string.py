class Solution:
    def checkValidString(self, s: str) -> bool:
        open_brackets = []
        asterisk = []

        for idx, c in enumerate(s):
            if c == ')':
                # Preferably use the opening brackets to match closing brackets first
                if open_brackets:
                    open_brackets.pop()
                elif asterisk:
                    asterisk.pop()
                else:
                    return False
            elif c == '(':
                open_brackets.append(idx)
            else:
                asterisk.append(idx)

        while open_brackets:
            idx = open_brackets.pop()
            # There are no asterisk to match opening brackets
            if not asterisk or asterisk.pop() < idx:
                return False
        return True
