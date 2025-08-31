class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0]*len(temperatures)
        st = []
        for i in range(len(temperatures)):
            while st and temperatures[st[-1]]<temperatures[i]:
                res = st.pop()
                ans[res] = i-res
            st.append(i)
        return ans
