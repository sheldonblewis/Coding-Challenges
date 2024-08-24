# Sub 30 mins, interview question

# Find longest palindromic substring of a given input string

class Solution:
    def longestPalindrome(self, s: str) -> str:
        for i in range(len(s)):
            for j in range(i+1):
                if (len(s)-i) % 2 == 1:
                    center = (len(s)-i)//2 + j
                    counter = 0
                    for k in range(1, (len(s)-i)//2+1):
                        if s[center+k] == s[center-k]:
                            counter += 1
                        else:
                            break
                    if counter == (len(s)-i)//2:
                        return s[j:j+len(s)-i]
                else:
                    center_r = (len(s)-i)//2 + j
                    counter = 0
                    for k in range((len(s)-i)//2):
                        if s[center_r+k] == s[center_r-k-1]:
                            counter += 1
                        else:
                            break
                    if counter == (len(s)-i)//2:
                        return s[j:j+len(s)-i]
