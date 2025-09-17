class TimeMap:

    def __init__(self):
        self.map = {}
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.map:
            self.map[key].append([timestamp,value])
        else:
            self.map[key]= [[timestamp,value]]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.map:
            return ""
        else:
            if not self.map[key]:
                return ""
            else:
                search_space = self.map[key]
                i = 0
                j = len(search_space)-1
                while i<=j:
                    mid = (i+j)//2
                    if search_space[mid][0]<=timestamp:
                        i=mid+1
                    else:
                        j=mid-1
                if search_space[j][0]<=timestamp:
                    return search_space[j][1]
                return ""
        

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)