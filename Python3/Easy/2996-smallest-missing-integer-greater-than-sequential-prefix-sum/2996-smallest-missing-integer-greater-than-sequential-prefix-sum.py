class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        n_sum: int = nums[0]
        for i in range(len(nums) - 1):
            if (nums[i] + 1) == nums[i + 1]:
                n_sum += nums[i + 1]
            else:
                break
        while n_sum in nums:
            n_sum += 1
        return (n_sum)
    