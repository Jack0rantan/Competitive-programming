class Cell:
    def __init__(self,x,y):
        self.data = x
        self.next = None        

    # アクセスメソッド
    # 先頭のセルを取り出すメソッド
    def first(self):
        return self.data
    # 先頭のセル以外のセルを取り出すメソッド
    def rest():
        return self.next
    
    # 破壊的メソッド being method
    # 　　--- オブジェクト自身を書き換えるメソッドのこと
    # 先頭のインスタンス変数を書き換えるメソッド
    def set_first(self, x):
        self.data = x
    # 先頭以降のセルの値を書き換えるメソッド
    def set_rest(self,x):
        self.next = x

class LinkedList:
    def __init__(self):
        self.top = None
    
    def insert(self, n, x):
        if n == 0 or not self.top:
            self.top = Cell(x, self.top)
        else:
            cp = self.top
            while cp.rest():
                n -= 1
                if n == 0: break
                cp = cp.rest()
            new_cp = Cell(x, cp.rest())
            cp.set_rest(new_cp)


if __name__ == "__main__":
    L = LinkedList()

    L.insert(3,1)
    
        
        
    

