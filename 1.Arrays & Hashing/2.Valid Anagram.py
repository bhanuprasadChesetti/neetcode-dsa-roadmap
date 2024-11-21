


# Problem: https://neetcode.io/problems/is-anagram



from collections import defaultdict


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        """
        Retrurns true if given strings s & t are anagrams, otherwise false.
        
        Time Complexity: O(n)
            - We iterate through the strings twice, so O(2n) ~ O(n).
        
        Space Complexity: O(1)
            - The maximum number of uniques keys that we store is 26 for given string of lenght n.       
        """


        s_length = len(s)

        t_length = len(t)


        if s_length != t_length:
            return False
        

        s_char_count = defaultdict(int)

        t_char_count = defaultdict(int)


        for i in range(s_length):

            s_char_count[s[i]] += 1

            t_char_count[t[i]] += 1

        

        for s_char,count in s_char_count.items():
            if (s_char not in t_char_count) or (count != t_char_count[s_char]):
                return False
            

        return True
            
