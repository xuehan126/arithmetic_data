class FindOnceChar:
    
    def __init__(self):
        self.s = ""
        self.dict = {}

    def FirstApperence(self):
        for i in self.s:
            if self.dict[i] == 1:
                return i

    def Insert(self, char):
        self.s = self.s + char
        if char in self.dict:
            self.dict[char] = self.dict[char] + 1
        else:
            self.dict[char] = 1

def findOnceTime(char):
    char_list = [i for i in char]
    char_dict = {}
    for x in char_list:
        dic = {x: char_list.count(x)}
        char_dict.update(dic)
    print(char_dict)
    for x in char_dict:
        if char_dict[x] == 1:
            yield x
print([x for x in findOnceTime("xuehan@12345xuehan")])
