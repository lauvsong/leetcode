from collections import Counter, defaultdict

class Solution:

    def isAnswer(self, counts, tSet, tCounts):
        for alpha in tSet:
            if counts[alpha] < tCounts[alpha]:
                return False
        return True

    def minWindow(self, s: str, t: str) -> str:
        res = ""

        l = r = 0
        tSet = set(t)
        tCounts = Counter(t)

        counts = defaultdict(int)
        counts[s[r]] += 1

        while l <= r and r != len(s):
            if self.isAnswer(counts, tSet, tCounts):
                if res == "" or len(res) > (r - l + 1):
                    res = s[l:r+1]
                
                counts[s[l]] -= 1
                l += 1
            else:
                r += 1
                if r != len(s):
                    counts[s[r]] += 1
        
        return res

        
"""
Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

 

Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.
Example 3:

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.
 

Constraints:

m == s.length
n == t.length
1 <= m, n <= 105
s and t consist of uppercase and lowercase English letters.

"""