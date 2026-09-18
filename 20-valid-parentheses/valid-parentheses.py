class Solution:
    def isValid(self, s: str) -> bool:
        st=[]
        for ch in s:
            if ch=='(':
                st.append('(')
            elif ch=='{':
                st.append('{')
            elif ch=='[':
                st.append('[')
            else:
                if not st:
                    return False
                else:
                    if ch==')' and st[-1]=='(':
                        st.pop()
                    elif ch=='}' and st[-1]=='{':
                        st.pop()
                    elif ch==']' and st[-1]=='[':
                        st.pop()
                    else:
                        return False
        return not st
