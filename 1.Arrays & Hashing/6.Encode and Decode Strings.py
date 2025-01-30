
# Problem: https://neetcode.io/problems/string-encode-and-decode

from typing import List

class Solution:

    delimiter = "#"

    def encode(self, strs: List[str]) -> str:

        encoded_str = ""

        for word in strs:
            encoded_str += f"{str(len(word))}{self.delimiter}{word}"

        return encoded_str
    
    def decode(self, s: str) -> List[str]:
        
        decoded_list = []

        word_length = ""
    
        i = 0

        while(i<len(s)):
            
            char = s[i]

            if char == self.delimiter:
                
                word_length = int(word_length)

                word = s[i+1:i+1+word_length]

                decoded_list.append(word)

                i = i+1+word_length

                word_length = ""
            else:
                word_length += char
                i += 1

        
        return decoded_list



