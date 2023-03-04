#Creating Generator iterators
def sequence_generator(sequence):
    for item in sequence:
        yield item

sequence_generator([1,2,3,4])

for number in sequence_generator([1,2,3,4]):
    print(number)


#Using gen expressions to create iterators
[item for item in [3,4,5,6]]#list comprehension

(item for item in[3,2,4,5,7])#generator expression

generator_expressiom=(item for item in[6,8,9,5])
for item in generator_expressiom:
    print(item)


#Different types of of generator itearators
def square_generator(sequence):
    for item in sequence:
        yield item**2

for square in square_generator([10,23,43,54,95]):
    print(square)


#fibonacci
def fibonacci_generator(stop=10):
    current_fib, next_fib=0,1
    for _ in range(0,stop):
        fib_number=current_fib
        current_fib, next_fib=(
            next_fib, current_fib+next_fib
        )
        yield fib_number


li=list(fibonacci_generator())
print(li)

print(list(fibonacci_generator(20)))

# when the loop finishes, the generator iterator automatically raises a StopIteration exception
def fibonacci_generator(stop=10):
    current_fib, next_fib = 0, 1
    index = 0
    while True:
        if index == stop:
            return
        index += 1
        fib_number = current_fib
        current_fib, next_fib = next_fib, current_fib + next_fib
        yield fib_number
        
print(fibonacci_generator(9))