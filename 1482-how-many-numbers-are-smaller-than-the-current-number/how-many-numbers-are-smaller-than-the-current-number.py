class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums)
        hash_count = {}
        for i, val in enumerate(sorted_nums):
            if val not in hash_count:
                hash_count[val] = i
        
        ans = []

        for i in nums:
            ans.append(hash_count[i])

        return ans