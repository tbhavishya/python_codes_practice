class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dct = {} #initiate a empty dictionary
        start, max_ = 0, 0 
      for i in range(len(s)): 
          if s[i] in dct:
               start = max(start, dct[s[i]]+1)
            max_ = max(max_, i-start+1)
            dct[s[i]] = i
          return max_

