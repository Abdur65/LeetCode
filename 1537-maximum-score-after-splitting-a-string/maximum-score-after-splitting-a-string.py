class Solution:
    def maxScore(self, s: str) -> int:
        n = len(s)
        cnt1 = 0
        mx = 0
        cnt = 0

        for i in s:
            if i == '1':
                cnt1 += 1

        for i in range(n-1):
            if s[i] == '0':
                cnt += 1
            else:
                cnt1 -= 1

            mx = max(mx, cnt1+cnt)

        return mx