#link: https://leetcode.com/problems/product-of-the-last-k-numbers
#had to go over failed testcases
#need to figure out edge cases before the problem
class ProductOfNumbers:

    def __init__(self):
        self.stream = []
        self.prefix = []
        self.zero_idx = -1
        
    def add(self, num: int) -> None:
        self.stream.append(num)
        if self.prefix:
            if num==0:
                self.zero_idx=len(self.stream)-1
                self.prefix.append(1)
            else:
                self.prefix.append(self.prefix[-1]*num)
        else:
            if num==0:
                self.zero_idx=len(self.stream)-1
                self.prefix.append(1)
            else:
                self.prefix.append(num)

    def getProduct(self, k: int) -> int:
        i=len(self.stream)
        first = i-k
        if self.zero_idx>=first:
            return 0
        else:
            if k==1:
                return self.stream[-1]
            if k==len(self.stream):
                return self.prefix[-1]
            
            return self.prefix[-1]//self.prefix[first-1]



# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
