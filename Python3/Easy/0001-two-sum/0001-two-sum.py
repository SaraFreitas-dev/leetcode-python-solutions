class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        leftover: int = 0

        for i, num in enumerate(nums):
            leftover = target - num

            if leftover in nums:
                j = nums.index(leftover)
                if i != j:
                    return [i, j]

