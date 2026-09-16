class Solution:
    def isValid(self, s: str) -> bool:
        ms = []
        hashmap = {"}":"{", "]":"[", ")":"("}
        for char in s:
            if char in hashmap.keys():
                if ms and ms[-1] == hashmap[char]:
                    ms.pop()
                else:
                    return False
                
            else:
                ms.append(char)
        return len(ms) == 0
        