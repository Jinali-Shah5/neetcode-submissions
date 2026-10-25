class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered = ''
        for c in s.lower():
            if c.isalnum():
                filtered = filtered + c
        return filtered == filtered[::-1]
        