class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        cols = len(encodedText) // rows

        original = []
        for col in range(cols):
            row = 0
            while row < rows and col < cols:
                idx = row * cols + col
                original.append(encodedText[idx])
                row += 1
                col += 1

        return "".join(original).rstrip()
