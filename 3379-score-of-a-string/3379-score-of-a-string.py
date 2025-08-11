class Solution:
    def scoreOfString(self, s: str) -> int:
        asci = []
        ans = 0
        for char in s:
            asci.append(ord(char))
        for i in range(0,len(asci)-1):
            ans += abs(asci[i] - asci[i+1])
        return ans