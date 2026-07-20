class Solution:
    def isPalindrome(self, s: str) -> bool:
        b="".join(char for char in s if char.isalnum())

        b=b.lower()

        c=b[::-1]
        if c==b:
            return True
        else:
            return False