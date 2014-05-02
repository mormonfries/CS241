import math

def parentindex( curindex):
    return (curindex - 1) // 2

def leftchild( i ):
    return i*2 + 1

class PriorityQueue ( object ):
    """ A priority queue implemented by a list heap"""

    def __init__(self):
        self.a = [None]

    def insert(self, value):
        # insert initial node into priority queue
        self.a.append(value)
        i = len(self.a) - 1
        while i//2 > 0:
            if self.a[i//2] > self.a[i]:
                swap = self.a[i//2]
                self.a[i//2] = self.a[i]
                self.a[i] = swap
            i //= 2


    def remove(self):
        """ Returns the top element, places the bottom element to the top of
        the tree and the tree of then reheapify from the top"""
        # WRITE THIS FUNCTION
        if len(self.a) > 1:
            ret = self.a[1]
            self.a[1] = self.a[-1]
            self.a.pop()
            self.reheapify(1)
            return ret
        else:
            del self.a[0]

    def reheapify(self, i):
        """ checks if the left or right is smaller than the top, and flips the position """
        # WRITE THIS FUNCTION
        if i*2 < len(self.a):
            if self.a[i*2] < self.a[i]:
                swap = self.a[i*2]
                self.a[i*2] = self.a[i]
                self.a[i] = swap
                self.reheapify(i*2)
            else:
                pass
        else:
            pass
        if (i*2)+1 < len(self.a):
            if self.a[(i*2)+1] < self.a[i]:
                swap = self.a[(i*2)+1]
                self.a[(i*2)+1] = self.a[i]
                self.a[i] = swap
                self.reheapify((i*2)+1)
            else:
                pass
        else:
            pass

    def __len__(self):
        """ returns the length of the heap """
        return len(self.a)

    def __str__(self):
        """ returns the comma seperated values for the heap """
        return ",".join(map(str,self.a))

if __name__ == "__main__":
    p = PriorityQueue()
    p.insert(30)
    p.insert(10)
    p.insert(80)
    p.insert(60)
    p.insert(20)
    p.insert(30)
    while len(p):
        # print p
        print p.remove()