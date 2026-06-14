class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        counter: int = 0
        if nums == sorted(nums):
            return 0
        while nums != sorted(nums):
            min_sum: int = inf
            min_index: int = 0

            for i in range(len(nums) - 1):
                current_sum: int = nums[i] + nums[i + 1]
                if current_sum < min_sum:  # Find the minimum sum
                    min_sum = current_sum
                    min_index = i

            nums_lst: list[int] = []
            for j in range(len(nums)):
                if j != min_index and j != (min_index + 1):
                    nums_lst.append(nums[j])
                elif j == min_index:
                    nums_lst.append(min_sum)
                else:
                    continue
            counter += 1
            nums = nums_lst
        return counter
        