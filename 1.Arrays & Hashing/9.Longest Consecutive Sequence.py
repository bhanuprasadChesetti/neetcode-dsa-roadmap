

# Problem: https://neetcode.io/problems/longest-consecutive-sequence


from typing import List



class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        

        nums.sort()

        max_seq_len = 0
        current_seq_len = 0
        seq_ends = float('-inf')

        for num in nums:

            if seq_ends+1 == num:
                current_seq_len += 1
                seq_ends = num
            elif num != seq_ends:
                
                if current_seq_len > max_seq_len:
                    max_seq_len = current_seq_len
                
                seq_ends = num
                current_seq_len = 1


        if current_seq_len > max_seq_len:
            max_seq_len = current_seq_len

        return max_seq_len

