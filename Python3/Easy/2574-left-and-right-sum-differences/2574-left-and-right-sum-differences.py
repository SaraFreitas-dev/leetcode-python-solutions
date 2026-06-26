class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        leftSum: list[int] = []
        rightSum: list[int] = []
        res: list[int] = []

        if len(nums) <= 1:
            res.append(0)
            return res

        # Get the list for leftSum and rightSum
        for i in range(len(nums)):
            n1: int = 0
            n2: int = 0

            if i == 0:
                leftSum.append(n1)
            else:
                pos: int = i - 1
                while pos >= 0:
                    n1 += nums[pos]
                    pos -= 1
                leftSum.append(n1)
            if i == len(nums):
                rightSum.append(n2)
            else:
                pos = i + 1
                while pos < len(nums):
                    n2 += nums[pos]
                    pos += 1
                rightSum.append(n2)

        for j in range(len(leftSum)):
            if leftSum[j] > rightSum[j]:
                res.append(leftSum[j] - rightSum[j])
            else:
                res.append(rightSum[j] - leftSum[j])
        return res