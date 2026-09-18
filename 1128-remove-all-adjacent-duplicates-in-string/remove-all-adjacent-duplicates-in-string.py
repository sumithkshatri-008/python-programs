class Solution:
    def removeDuplicates(self, s: str) -> str:
        st=[]
        for ch in s:
            if not st:
                st.append(ch)
            else:
                if st[-1]==ch:
                    st.pop()
                else:
                    st.append(ch)
        return ''.join(st)

        