class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        my_array = []
        i = 0
        while i < len(s):
            k = i
            while s[k] != '#':
                k += 1
            start = k + 1
            end = start + int(s[i:k])

            my_array.append(s[start:end])
            i = end
        return my_array

