class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums_sum = sum(nums)
        n = len(nums)
        actual_sum = int((n*(n+1))/2)

        return actual_sum - nums_sum 