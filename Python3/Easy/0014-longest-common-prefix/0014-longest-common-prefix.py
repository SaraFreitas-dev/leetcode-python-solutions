class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        common_str: list[str] = []
        for i in range(len(strs[0])):
            same_letter: bool = True
            for string in strs[1:]:
                if i >= len(string) or strs[0][i] != string[i]:
                    same_letter = False
            if same_letter:
                common_str.append(strs[0][i])
            else:
                break
        return "".join(common_str)

