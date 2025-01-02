import random
class RandomizedSet:

    def __init__(self):
        self.datamap = {}
        self.data = []
        return

    def insert(self, val: int) -> bool:
        if val not in self.datamap.keys():
            self.datamap[val] = len(self.data)
            self.data.append(val)
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        if val in self.datamap.keys():
            vidx = self.datamap[val]
            if vidx != len(self.data)-1: # 마지막 index이 아닌 경우
                val2 = self.data.pop(val)
                self.data[vidx] = val2
                self.datamap[val2] = vidx
            else: # 마지막 index인 경우
                self.data.pop()
            self.datamap.pop(val)
            return True
        else:
            return False

    def getRandom(self) -> int:
        return random.choice(self.data)
