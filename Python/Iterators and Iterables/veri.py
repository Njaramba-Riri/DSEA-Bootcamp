from sequence_iter import SequenceIterator

for item in SequenceIterator([1,2,3,4,5]):
    print(item)


from square_iter import SquareIterator

for square in SquareIterator([1,2,3,6,8,9,50]):
    print (square)


from fib_iter import FibonacciIterator

for fib_num in FibonacciIterator():
    print(fib_num)

#from inf_iter import FibonnaciIterator

#for fib_no in FibonnaciIterator():
#    print(fib_no)