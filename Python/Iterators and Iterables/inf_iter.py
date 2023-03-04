#coding potentially infinite iterators

class FibonnaciIterator:
    def __init__(self):
        self._index=0
        self._current=0
        self._next=1

    def __iter__(self):
        return self
    
    def __next__(self):
        self._index +=1
        self._current, self._next=(self._next, self._current+self._next)
        return self._current
    
    

#  .__next__() never raises a StopIteration exception. This fact turns the instances of this class into potentially infinite iterators that would produce values forever if you used the class in a for loop.
