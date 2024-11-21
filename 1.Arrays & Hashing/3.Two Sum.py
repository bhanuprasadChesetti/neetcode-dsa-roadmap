

# Problem: https://neetcode.io/problems/two-integer-sum

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        """
        Returns pair of indices whose sum is target.

        - Time Complexity: O(n)

        - Space Complexity: O(n)

        """
        
        nums_index_map = {}

        for i in range(len(nums)):

            num = nums[i]

            value_required_to_target = target - num

            if value_required_to_target in nums_index_map:
                return sorted([i,nums_index_map[value_required_to_target]])
            else:
                nums_index_map[num] = i
        


