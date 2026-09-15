class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = Counter(nums)
        my_array = []
        
        for i in range(k):
            max_key = None
            max_value = -1

            for key, value in hashmap.items():
                if value > max_value:
                    max_value = value
                    max_key = key
            
            my_array.append(max_key)
            hashmap.pop(max_key)
        
        return my_array


        