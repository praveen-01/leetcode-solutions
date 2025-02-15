#link: https://leetcode.com/problems/find-the-punishment-number-of-an-integer
#generating bruteforce should work
#problem is with generating all partitions of the number
class Solution:
    def punishmentNumber(self, n: int) -> int:
        def generate_number(i,cur,target,string):
            if i==len(string) and cur==target:
                return True
            for j in range(i,len(string)):
                if generate_number(j+1,cur+int(string[i:j+1]),target,string):
                    return True
            return False 
            
        ans=0
        for i in range(1,n+1):
            sq = i*i
            if generate_number(0,0,i,str(sq)):
                ans+=sq
        return ans

        

        
