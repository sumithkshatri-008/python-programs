def is_v(ch):
    return ch in "aeiou"
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        mx=0
        first_window=s[:k]
        count=0
        for i in first_window:
            if is_v(i):
                count+=1
        mx=max(count,mx)
        for i in range(k,len(s)):
            if is_v(s[i]):
                count+=1
            if is_v(s[i-k]):
                count-=1
            mx=max(mx,count)

        return max(mx, count)



        