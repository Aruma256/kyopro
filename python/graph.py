class UnionFindEx:
    def __init__(self, size):
        #正なら根の番号、負ならグループサイズ
        self.roots = [-1] * size
    def getRootID(self, i):
        r = self.roots[i]
        if r < 0:   #負なら根
            return i
        else:
            r = self.getRootID(r)
            self.roots[i] = r
            return r
    def getGroupSize(self, i):
        return -self.roots[self.getRootID(i)]
    def connect(self, i, j):
        r1, r2 = self.getRootID(i), self.getRootID(j)
        if r1 == r2:
            return False
        if self.getGroupSize(r1) < self.getGroupSize(r2):
            r1, r2 = r2, r1
        self.roots[r1] += self.roots[r2]    #サイズ更新
        self.roots[r2] = r1
        return True
