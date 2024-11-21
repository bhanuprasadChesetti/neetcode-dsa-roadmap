
# Problem: https://leetcode.com/problems/contains-duplicate/


from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        """
        Returns true if the input list contains duplicate elements, otherwise false.
        
        Time Complexity: O(n)
            - We iterate through the list once.
            - Each membership check and addition operation in a set is O(1) on average.
        
        Space Complexity: O(n)
            - In the worst case, all elements in the list are unique, 
              so we store all of them in the `visited` set.
        """
        
        visited = set()

        for num in nums:

            if num not in visited:
                visited.add(num)
            else:
                return True
        
        return False
    





