class LinearList:
    def __init__(self, maxSize = 4):
        self.capacity = maxSize # 最大容量
        self.data = [None] * self.capacity # 用列表存储线性表的元素
        self.size = 0 # 记录线性表的长度

    def search(self, x):
        for i in range(self.size):
            if self.data[i] == x:
                return i
        return -1 # 如果元素不存在，返回-1
    
    def insert(self, i, x):
        if self.size == self.capacity:
            self.double_space()
        if 0 <= i <= self.size:
            for j in range(self.size, i, -1):
                self.data[j] = self.data[j - 1]
            self.data[i] = x
            self.size += 1
        else:
            raise IndexError("Invalid index")
        
    def length(self):
        return self.size
    
    def clear(self):
        self.size = 0

    def remove(self, i):
        #TODO
        return None

    def visit(self, i):
         #TODO
        return None

    def traverse(self):
         #TODO
        return None
    
    
a = LinearList()
a.insert(0, 1)
a.insert(1, 2)
print(a.search(0), a.search(1))
 