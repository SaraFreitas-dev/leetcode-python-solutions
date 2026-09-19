class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)

"""
To practice the logic instead:
    for i in range(len(haystack)):
        if haystack[i:i + len(needle)] == needle:
            return (i)
    return (-1)
"""