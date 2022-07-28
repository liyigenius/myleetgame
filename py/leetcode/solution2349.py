from sortedcontainers import SortedList
class NumberContainers:

    def __init__(self):
        self.m1 = {}
        self.ll = {}


    def change(self, index: int, number: int) -> None:
        if index not in self.ll:
            self.ll[index] = number
        else:
            prev = self.ll[index]
            self.ll[index] = number
            prevSd = self.m1[prev]
            prevSd.remove(index)

        if number not in self.m1:
            sd1 = SortedList()
            sd1.add(index)
            self.m1[number] = sd1
        else:
            self.m1[number].add(index)




    def find(self, number: int) -> int:
        if number not in self.m1:
            return -1
        if len(self.m1[number]) == 0:
            return -1
        return self.m1[number][0]


"""
["NumberContainers","change","find","change","find","find","find"]
[[],[1,10],[10],[1,20],[10],[20],[30]]
"""
# Your NumberContainers object will be instantiated and called as such:
obj = NumberContainers()
obj.change(1,10)
obj.find(10)
obj.change(1,20)
obj.find(10)
# obj.change(index,number)
# param_2 = obj.find(number)