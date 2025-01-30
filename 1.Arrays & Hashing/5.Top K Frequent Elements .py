
# Problem: https://neetcode.io/problems/top-k-elements-in-list


from typing import List
from collections import Counter



class Solution:

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
      
        nums_freq = Counter(nums)

        freq_index_array = [[] for _ in range(len(nums) + 1)]

        for num,freq in nums_freq.items():
            freq_index_array[freq].append(num)

        topK = []

        for i in range(len(freq_index_array)-1,0,-1):
            if len(freq_index_array[i]) > 0:
                topK.extend(freq_index_array[i])

                if len(topK) == k:
                    break

        return topK
   

            
        