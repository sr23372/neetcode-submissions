class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L, R = 0, len(nums) - 1
        while L <= R:
            if nums[L] == target:
                return L
            if nums[R] == target:
                return R
            
            middle = (L + R) // 2

            if nums[middle] == target:
                return middle
            if nums[middle] < target:
                L = middle + 1
            if nums[middle] > target:
                R = middle - 1
            
        return -1


            

            
        