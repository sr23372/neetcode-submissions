class Solution:
    def isPalindrome(self, s: str) -> bool:
        reverse = ""
        alphaNumericString = ""
        
        for char in s:
            if char.isalnum():
                alphaNumericString += char.lower()
        for char in s[::-1]:
            if char.isalnum():
                reverse += char.lower()

        return reverse == alphaNumericString
        