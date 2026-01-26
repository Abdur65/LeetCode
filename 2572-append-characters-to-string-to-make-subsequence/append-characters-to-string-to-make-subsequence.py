class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        q = 0

        for i in range(len(s)):
            if t[q] == s[i]:
                q += 1
            
            if q == len(t):
                return 0
            
        return len(t) - q