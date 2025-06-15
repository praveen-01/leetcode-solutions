'''
for maximum number that we can get, pick the first number which is not 9 and replace that across x with 9
for minimum number that we can get,pick the first number which is not 0 and replace that across x with 1
return res=max-min from the above 2 steps
'''
class Solution:
    def num_to_arr(self,num):
        num_list = []
        while num:
            rem = num%10
            num_list.append(rem)
            num//=10
        return num_list[::-1]

    def maxDiff(self, num: int) -> int:
        num_list = self.num_to_arr(num)
        max_num = 0
        min_num = 0
        found_max = -1
        found_min = -1
        for i in num_list:
            if i!=9:
                if found_max==-1:
                    found_max=i
            if i!=1 and i!=0:
                if found_min==-1:
                    found_min=i
                    idx = num_list.index(i)
                    
            if i==found_max:
                max_num = max_num*10+9
            else:
                max_num = max_num*10+i
            if i==found_min:
                if idx!=0:
                    min_num = min_num*10
                else:
                    min_num = min_num*10+1
            else:
                min_num = min_num*10+i
        return max_num-min_num

        
