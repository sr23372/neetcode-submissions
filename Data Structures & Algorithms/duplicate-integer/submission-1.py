class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset = {}
        for number in nums:
            if number in hashset:
                return True
            else:
                hashset[number] = hashset.get(number, 0)  + 1

        return False
        