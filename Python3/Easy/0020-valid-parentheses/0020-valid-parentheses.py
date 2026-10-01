class Solution:
    def isValid(self, s: str) -> bool:
        stack: list = []
        pairs: dict[str, str] = {
            "(": ")",
            "[": "]",
            "{": "}"
        }

        for bracket in s:
            if bracket in pairs:
                stack.append(bracket)
            elif bracket in pairs.values():
                if not stack:
                    return False
                elif pairs[stack.pop()] != bracket:
                    return False
        return not stack