#Given an array of integers, find the sum of its elements. For example, if the array ar = [1,2,3],Calculate 1+2+3 = 6, so return 6.

#asks user to input array elements and then it retuns a list
def ask_array():
    li=list(map(int,input("array elements: ").strip().split()))
    return li

#takes a single iterable argument and returns the sum of those values
def summation(arr):
    return sum(arr)


#High-order function that takes 2 args, function `f` and a variable-length argument `*args`
def main(f, *args):
    result=f(*args)
    print(f"The sum of the array elements= {result}")


# checks whether the  module is being run as the main program or if it is being imported as a module into another program
if __name__=="__main__":
    main(summation, ask_array())
  