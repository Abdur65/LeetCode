class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        set_len = len(set(nums))

        if set_len == len(nums):
            return False
        else:
            return True