#link: https://leetcode.com/problems/design-a-number-container-system
class NumberContainers:

    def __init__(self):
        self.container={}
        self.number={}

    def change(self, index: int, number: int) -> None:
        if index in self.container and self.container[index]==number: return
        self.container[index]=number
        if number not in self.number:
            self.number[number]=[]
        heapq.heappush(self.number[number],index)

    def find(self, number: int) -> int:
        if number not in self.number:
            return -1
        else:
            print(self.container)
            print(self.number)
            while self.number[number] and self.container[self.number[number][0]]!=number:
                heapq.heappop(self.number[number])
            return self.number[number][0] if self.number[number] else -1
        


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)
