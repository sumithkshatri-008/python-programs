class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        char=list(s)
        left,right=0,len(char)-1
        while left<right:
            if not char[left].isalpha():
                left+=1
            elif not char[right].isalpha():
                right-=1
            else:
                char[left], char[right]=char[right],char[left]
                left+=1
                right-=1
        return ''.join(char)
        