
# Problem: https://neetcode.io/problems/products-of-array-discluding-self

from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        output = [1]

        prefix = 1

        for i in range(0,len(nums)-1):
            prefix *= nums[i]
            output.append(prefix)

        suffix = 1
        for i in range(len(nums)-1,0,-1):
            suffix *= nums[i]
            output[i-1] = output[i-1]*suffix

        return output 
