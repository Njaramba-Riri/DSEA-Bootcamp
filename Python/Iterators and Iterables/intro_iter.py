#repetitive code, hard to maintain and not scalable
print("Hello")
print("Hello")
print("Hello")
print("Hello")

#indefinite iteration
#using loops to solve the issue
times=0

while times<4:
    print("Hello")
    times +=1

#definite iteration
nums=[1,2,3,4,5,6,7]

for n in nums:
    print(n)



#how do for loops work internally?
from sequence_iter import SequenceIterator

sequence=SequenceIterator([1,2,3,4,5,5])

#get an iterator over the data
iterator=sequence.__iter__()
while True:
    try:
        #Retrieve the next item
        item=iterator.__next__()
    except StopIteration:
        break
    else:
        #The loop's code goes here...
        print(item)