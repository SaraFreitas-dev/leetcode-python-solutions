class Solution:
    def romanToInt(self, s: str) -> int:
        roman_values: dict[str, int] = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        total: int = 0

        for i in range(len(s) - 1):
            current: int = roman_values[s[i]] 
            next_v: int = roman_values[s[i + 1]]
            if current < next_v:
                total -= current
            else:
                total += current
        if s:
            total += roman_values[s[-1]]
        return total