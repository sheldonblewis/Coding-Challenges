class Solution:
    def countSubstrings(self, s: str) -> int:
        counter = 0
        for i in range(len(s)):
            left = i
            right = i
            while left >= 0 and right < len(s):
                if s[left] == s[right]:
                    counter += 1
                    left -= 1
                    right += 1
                else:
                    break
        for i in range(len(s)-1):
            left = i
            right = i+1
            while left >= 0 and right < len(s):
                    if s[left] == s[right]:
                        counter += 1
                        left -= 1
                        right += 1
                    else:
                        break
        return counter
