class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, j in enumerate(nums):
            numb = target - nums[i]
            if numb in seen:
                return [seen[numb],i]
            seen[j] = i

        return [-1,-1]
            