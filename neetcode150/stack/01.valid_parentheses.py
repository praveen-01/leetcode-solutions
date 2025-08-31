class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        op = "({["
        mapping = {")":"(","}":"{","]":"["}
        for i in s:
            if i in op:
                st.append(i)
            else:
                if not st: return False
                tk = st.pop(-1)
                if mapping[i]!=tk:
                    return False
        return not st
