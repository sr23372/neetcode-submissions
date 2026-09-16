class Solution:
    def isValid(self, s: str) -> bool:
        ms = []
        hashmap = {"}":"{", "]":"[", ")":"("}
        for char in s:
            if char in hashmap.keys():
                if len(ms) == 0:
                    return False
                rc = ms.pop()
                if rc != hashmap.get(char):
                    return False
            else:
                ms.append(char)
        return len(ms) == 0
        