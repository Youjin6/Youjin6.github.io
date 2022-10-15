class RandomizedSet:

    def __init__(self):
        self.dic = {}
        self.arr = []

    def insert(self, val: int) -> bool:
        if val not in self.dic:
            self.arr.append(val)
            self.dic[val] = len(self.arr) - 1
            
            return True
        return False
    
    def remove(self, val: int) -> bool:
        if val in self.dic:
            val_idx = self.dic[val]
            last_num = self.arr[-1]

            self.arr[val_idx] = last_num
            self.arr.pop()
            self.dic[last_num] = val_idx
            del self.dic[val]
            return True
        
        return False
        

    def getRandom(self) -> int:
        return choice(self.arr)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()