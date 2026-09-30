class Solution:
    def separateDigits(self, nums: list[int]) -> list[int]:
        res: list = []
        for i in range(len(nums)):
            res.extend([int(digit) for digit in str(nums[i])])
        return (res)
