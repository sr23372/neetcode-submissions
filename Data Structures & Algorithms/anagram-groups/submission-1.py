class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_dict = {}
        for string in strs:
            #represent the string as a counter of characaters
            temp = [0]*26
            for char in string:
                temp[ord(char) - ord('a')]  += 1

            key = tuple(temp)
            if key not in my_dict:
                my_dict[key] = []

            my_dict[key].append(string)
        return list(my_dict.values())


            
            
            
            
                
            
                

        