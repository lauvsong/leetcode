from collections import Counter

class Solution:
    def longestPalindrome(self, s: str) -> int:
        res = 0
        counts = Counter(s)
        
        for letter, count in counts.items():
            res += count if count & 1 == 0 else count-1
            if res & 1 == 0 and count & 1:
                res += 1
        
        return res

"""
Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.

Letters are case sensitive, for example, "Aa" is not considered a palindrome here.

 

Example 1:

Input: s = "abccccdd"
Output: 7
Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.
Example 2:

Input: s = "a"
Output: 1
Explanation: The longest palindrome that can be built is "a", whose length is 1.
 

Constraints:

1 <= s.length <= 2000
s consists of lowercase and/or uppercase English letters only.
"""