class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_tab = {}

        for i, val in enumerate(nums):
            dif = target - val
            if dif in hash_tab:
                j = hash_tab[dif]
                ans = [i, j]
                return ans

            hash_tab[val] = i