class MedianFinder:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.h_hi = []
        self.h_lo = []
        
    def addNum(self, num):
        """
        Adds a num into the data structure.
        :type num: int
        :rtype: void
        """
        self.h_hi.append(num)
        self.swim_hi(0,len(self.h_hi)-1)
        if len(self.h_hi) - len(self.h_lo) > 1:
            self.h_lo.append(self.pop(self.h_hi))
            self.swim_lo(0,len(self.h_lo)-1)
        if len(self.h_hi) > 0 and len(self.h_lo) >0:
            if self.h_hi[0] < self.h_lo[0]:
                self.h_hi[0],self.h_lo[0] = self.h_lo[0],self.h_hi[0]
                self.sink_hi(0,len(self.h_hi)-1)
                self.sink_lo(0,len(self.h_lo)-1)
        print self.h_lo
        print self.h_hi
        print
    def findMedian(self):
        """
        Returns the median of current data stream
        :rtype: float
        """
        if len(self.h_lo) == 0:
            return self.h_hi[0]
        if ((len(self.h_hi) + len(self.h_lo)) % 2) == 0:
            return float((self.h_hi[0] + self.h_lo[0]))/2
        else:
            return self.h_hi[0]
    def swim_hi(self,s,e):
        if e <= s:
            return
        if e%2 == 0:
            p = (e/2)-1
        else:
            p = (e-1)/2
        if self.h_hi[p] > self.h_hi[e]:
            temp = self.h_hi[p]
            self.h_hi[p] = self.h_hi[e]
            self.h_hi[e] = temp
            self.swim_hi(s,p)
    def swim_lo(self,s,e):
        if e <= s:
            return 
        if e%2 == 0:
            p = (e/2)-1
        else:
            p = (e-1)/2
        if self.h_lo[p] < self.h_lo[e]:
            temp = self.h_lo[p]
            self.h_lo[p] = self.h_lo[e]
            self.h_lo[e] = temp
            self.swim_lo(s,p)
    def pop(self,arr):
        if self.h_hi == arr:
            temp = self.h_hi[0]
            self.h_hi[0] = self.h_hi[-1]
            self.h_hi = self.h_hi[:-1]
            self.sink_hi(0,len(self.h_hi)-1)
        return temp
    def sink_hi(self,s,e):
        if e <= s:
            return
        c1 = (s*2)+1
        c2 = (s*2)+2
        if c1 >= len(self.h_hi):
            return
        elif self.h_hi[c1] < self.h_hi[s] and c2 >= len(self.h_hi):
                temp = self.h_hi[s]
                self.h_hi[s] = self.h_hi[c1]
                self.h_hi[c1] = temp
                self.sink_hi(c1,e)
        elif c2 < len(self.h_hi):
            if self.h_hi[c2] < self.h_hi[s] and self.h_hi[c2]<=self.h_hi[c1]:
                temp = self.h_hi[s]
                self.h_hi[s] = self.h_hi[c2]
                self.h_hi[c2] = temp
                self.sink_hi(c2,e)
            elif self.h_hi[c1] < self.h_hi[s] and self.h_hi[c1]<=self.h_hi[c2]:
                temp = self.h_hi[s]
                self.h_hi[s] = self.h_hi[c1]
                self.h_hi[c1] = temp
                self.sink_hi(c1,e)

    def sink_lo(self,s,e):
        if e <= s:
            return
        c1 = (s*2)+1
        c2 = (s*2)+2
        if c1 >= len(self.h_lo):
            return
        elif c2 >= len(self.h_lo):
            if self.h_lo[c1] > self.h_lo[s]:
                temp = self.h_lo[s]
                self.h_lo[s] = self.h_lo[c1]
                self.h_lo[c1] = temp
                self.sink_lo(c1,e)
        elif c2 < len(self.h_lo):
            if self.h_lo[c2] > self.h_lo[s] and self.h_lo[c2]>=self.h_lo[c1]:
                temp = self.h_lo[s]
                self.h_lo[s] = self.h_lo[c2]
                self.h_lo[c2] = temp
                self.sink_lo(c2,e)
            elif self.h_lo[c1] > self.h_lo[s] and self.h_lo[c1]>=self.h_lo[c2]:
                temp = self.h_lo[s]
                self.h_lo[s] = self.h_lo[c1]
                self.h_lo[c1] = temp
                self.sink_lo(c1,e)

mf= MedianFinder()


mf.addNum(78)
print mf.findMedian()
mf.addNum(14)
print mf.findMedian()
mf.addNum(50)
print mf.findMedian()
mf.addNum(20)
print mf.findMedian()
mf.addNum(13)
print mf.findMedian()
mf.addNum(9)
print mf.findMedian()
mf.addNum(25)
print mf.findMedian()
mf.addNum(8)
print mf.findMedian()
mf.addNum(13)
print mf.findMedian()
mf.addNum(37)
print mf.findMedian()
mf.addNum(29)
print mf.findMedian()
mf.addNum(33)
print mf.findMedian()
mf.addNum(55)
print mf.findMedian()
mf.addNum(52)
print mf.findMedian()
mf.addNum(6)
print mf.findMedian()
mf.addNum(17)
print mf.findMedian()
mf.addNum(65)
print mf.findMedian()
mf.addNum(23)
print mf.findMedian()
mf.addNum(74)
print mf.findMedian()
mf.addNum(43)
print mf.findMedian()
mf.addNum(5)
print mf.findMedian()
mf.addNum(29)
print mf.findMedian()
mf.addNum(29)
print mf.findMedian()
mf.addNum(72)
print mf.findMedian()
mf.addNum(7)
print mf.findMedian()
mf.addNum(13)
print mf.findMedian()
mf.addNum(56)
print mf.findMedian()
mf.addNum(21)
print mf.findMedian()
mf.addNum(31)
print mf.findMedian()
mf.addNum(66)
print mf.findMedian()
mf.addNum(69)
print mf.findMedian()
mf.addNum(69)
print mf.findMedian()
mf.addNum(74)
print mf.findMedian()
mf.addNum(12)
print mf.findMedian()
mf.addNum(77)
print mf.findMedian()
mf.addNum(23)
print mf.findMedian()
mf.addNum(10)
print mf.findMedian()
mf.addNum(6)
print mf.findMedian()
mf.addNum(27)
print mf.findMedian()
mf.addNum(63)
print mf.findMedian()
mf.addNum(77)
print mf.findMedian()
mf.addNum(21)
print mf.findMedian()
mf.addNum(40)
print mf.findMedian()
mf.addNum(10)
print mf.findMedian()
mf.addNum(19)
print mf.findMedian()
mf.addNum(59)
print mf.findMedian()
mf.addNum(35)
print mf.findMedian()
mf.addNum(40)
print mf.findMedian()
mf.addNum(44)
print mf.findMedian()
mf.addNum(4)
print mf.findMedian()
mf.addNum(15)
print mf.findMedian()
mf.addNum(29)
print mf.findMedian()
mf.addNum(63)
print mf.findMedian()
mf.addNum(27)
print mf.findMedian()
mf.addNum(46)
print mf.findMedian()
mf.addNum(56)
print mf.findMedian()
mf.addNum(0)
print mf.findMedian()

mf.addNum(60)
print mf.findMedian()
mf.addNum(72)
print mf.findMedian()
mf.addNum(35)
print mf.findMedian()
mf.addNum(54)
print mf.findMedian()
mf.addNum(50)
print mf.findMedian()
mf.addNum(14)
print mf.findMedian()
mf.addNum(29)
print mf.findMedian()
mf.addNum(62)
print mf.findMedian()
mf.addNum(24)
print mf.findMedian()
mf.addNum(18)
print mf.findMedian()
mf.addNum(79)
print mf.findMedian()
mf.addNum(16)
print mf.findMedian()
mf.addNum(19)
print mf.findMedian()
mf.addNum(8)
print mf.findMedian()
mf.addNum(77)
print mf.findMedian()
mf.addNum(10)
print mf.findMedian()
mf.addNum(21)
print mf.findMedian()
mf.addNum(66)
print mf.findMedian()
mf.addNum(42)
print mf.findMedian()
mf.addNum(76)
print mf.findMedian()
mf.addNum(14)
print mf.findMedian()
mf.addNum(58)
print mf.findMedian()
mf.addNum(28)
print mf.findMedian()
mf.addNum(0)
print mf.findMedian()

"""
mf.addNum(5)
print mf.findMedian()
mf.addNum(4)
print mf.findMedian()
mf.addNum(3)
print mf.findMedian()
mf.addNum(2)
print mf.findMedian()
mf.addNum(1)
print mf.findMedian()
"""
