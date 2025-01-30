


# Problem: https://neetcode.io/problems/anagram-groups


from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        
        anagram_group = {}


        for word in strs:
            
            code = self.get_unique_code(word)

            if code not in anagram_group:
                anagram_group[code] = []

            anagram_group[code].append(word)


        return list(anagram_group.values())
    

    def get_unique_code(self, word: str) -> str:
        
        code = ""

        if word == "":
            return "0"
        

        char_count = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}


        for char in word:
            char_count[char] += 1

        
        for char in "abcdefghijklmnopqrstuvwxyz":
            code = code + char + str(char_count[char])


        return code




