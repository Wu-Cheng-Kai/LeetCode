# 1. list >> O(N)
import random
class RandomizedSet:

    def __init__(self):
        self.list = []

    def insert(self, val: int) -> bool:
        if val in self.list:
            return False
        else:
            self.list.append(val)
            return True    

    def remove(self, val: int) -> bool:
        if val in self.list:
            self.list.remove(val)
            return True
        else:
            return False

    def getRandom(self) -> int:
        random_index = random.randint(0, len(self.list)-1)
        return self.list[random_index]
    
# 2. set >> O(N)
class RandomizedSet:

    def __init__(self):
        self.set = set()

    def insert(self, val: int) -> bool:
        if val in self.set:
            return False
        else:
            self.set.add(val)
            return True    

    def remove(self, val: int) -> bool:
        if val in self.set:
            self.set.remove(val)
            return True
        else:
            return False

    def getRandom(self) -> int:
        return random.choice(list(self.set))

# 3. list + dictionary      
class RandomizedSet:

    def __init__(self):
        self.index = {}
        self.value = []

    def insert(self, val: int) -> bool:
        if val in self.value:
            return False
        else:
            self.index[val] = len(self.value)
            self.value.append(val)
            return True    

    def remove(self, val: int) -> bool:
        if val in self.value:
            
            # change position between val and last value
            val_index = self.index[val]
            last_value = self.value[-1]
            self.value[val_index] = last_value
            self.index[last_value] = val_index
            
            # delete last value
            self.value.pop()
            del self.index[val]
            return True
        else:
            return False

    def getRandom(self) -> int:
        return random.choice(self.value)

param = [0] * 7
obj = RandomizedSet()
param[0] = obj.insert(1)
param[1] = obj.remove(2)
param[2] = obj.insert(2)
param[3] = obj.getRandom()
param[4] = obj.remove(1)
param[5] = obj.insert(2)
param[6] = obj.getRandom()

print(obj.index.items())
# print(obj.index[10])
print(param)