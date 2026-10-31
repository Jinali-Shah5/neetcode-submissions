class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = []
        index = -1
        for i,num in enumerate(nums):
            numb = target - num
            if numb in nums:
                index = nums.index(numb)
                if index != i:
                    ans =  [index,i]
        return ans
        