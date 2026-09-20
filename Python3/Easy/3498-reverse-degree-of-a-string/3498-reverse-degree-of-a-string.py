class Solution:
    def reverseDegree(self, s: str) -> int:
        total: int = 0

        for i, c in enumerate(s, start=1):
            alphabet_position = ord(c) - ord('a') + 1
            reverse_value = 27 - alphabet_position

            total += reverse_value * i

        return total