class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        
        s = ""
        for word in words:
            word_value = 0
            total = 0
            for c in word:
                word_value = (ord(c) - ord('a'))
                total += weights[word_value]
            s += chr(ord('z') - (total % 26))
        return s