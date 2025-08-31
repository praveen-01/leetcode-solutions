class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        op = "+-*/"
        for i in tokens:
            if i not in op:
                st.append(int(i))
                continue
            a = st.pop()
            b = st.pop()
            if i=="+":    
                st.append(a+b)
            elif i=="-":
                st.append(b-a)
            elif i=="*":
                st.append(a*b)
            else:
                st.append(int(b/a))
        return st[0]
