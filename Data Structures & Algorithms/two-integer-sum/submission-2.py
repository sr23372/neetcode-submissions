class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        difference = {}
        array_length = len(nums)
        for i in range(array_length):
            diff = target - nums[i]

            if diff in difference:
                return [difference.get(diff), i]   
            else:
                difference[nums[i]] = i

        return 
