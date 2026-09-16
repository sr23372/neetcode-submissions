class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        numSet = set(nums) #ignore duplicates
        for n in numSet:
            temp = 0
            cur = n
            if cur - 1 not in numSet:
                while cur in numSet:#start of sequence
                    temp += 1
                    cur += 1
            
            longest = max(temp, longest)
        return longest


