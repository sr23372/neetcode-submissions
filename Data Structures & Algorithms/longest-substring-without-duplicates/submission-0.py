class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longestSubStringLength = 0
        charSet = set()
        l, r = 0, 0
        for c in s:
            r += 1
            while c in charSet:
                temp = s[l]
                charSet.remove(temp)
                l += 1
            charSet.add(c)
            longestSubStringLength = max(longestSubStringLength, r - l)
        return longestSubStringLength

            
            

            


        