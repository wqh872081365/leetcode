"""
Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.

Examples:
[2,3,4] , the median is 3

[2,3], the median is (2 + 3) / 2 = 2.5

Design a data structure that supports the following two operations:

void addNum(int num) - Add a integer number from the data stream to the data structure.
double findMedian() - Return the median of all elements so far.
For example:

addNum(1)
addNum(2)
findMedian() -> 1.5
addNum(3)
findMedian() -> 2
"""

class MedianFinder(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.l = []

    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        if self.l:
            if num < self.l[0]:
                self.l.insert(0, num)
            elif num > self.l[-1]:
                self.l.append(num)
            else:
                start = 0
                end = len(self.l) - 1
                index = 0
                while start < end:
                    if num > self.l[(start + end) / 2]:
                        start = (start + end) / 2 + 1
                    elif num < self.l[(start + end) / 2]:
                        end = (start + end) / 2 - 1
                    else:
                        self.l.insert((start + end) / 2, num)
                        index = 1
                        break
                if not index:
                    if num > self.l[start]:
                        self.l.insert(start + 1, num)
                    else:
                        self.l.insert(start, num)
        else:
            self.l.append(num)

    def findMedian(self):
        """
        :rtype: float
        """
        length = len(self.l)
        if length % 2 == 0:
            return (self.l[length / 2 - 1] + self.l[length / 2]) / 2.
        else:
            return self.l[length / 2]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()