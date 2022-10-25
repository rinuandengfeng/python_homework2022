
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        subscript_total = len(nums)
        subscript_list = []
        for i in nums:
            # 获取元素下标
            subscript = nums.index(i)

            for a in nums[subscript+1:subscript_total+1]:
                if i + a == target:
                    subscript_a = nums.index(a)
                    subscript_list.append(subscript)
                    subscript_list.append(subscript_a)
                
        return subscript_list
    
s = Solution()
nums = list(input())
target = input()
print(s.twoSum(nums,target))