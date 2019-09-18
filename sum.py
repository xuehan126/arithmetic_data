#! /usr/bin/python
class Sum:
    def __init__(self):
        self.sum = 0
    
    def sum_(self, n):
        
        def zi_sum(n):
            self.sum += n
            n-=1
            # print("返回值为：", bool(n>0 and self.sum_(n)))
            # print(bool(n>0 and self.sum_(n)))
            return n>0 and self.sum_(n)
        # print("the zi_sum(%d) is "%n, zi_sum(n))
        zi_sum(n)
        return self.sum
print("总数之和为：", Sum().sum_(100))
