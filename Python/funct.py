def hello_world(h):
  def world(w):
        print(h, w)
  return world # returning functions

h = hello_world # assigning
x = h("hello") # assigning
x

x("world")





list(map(int, ['1','2','3']))

function_list=[h,x]
function_list



#python functonality purity
def native_sum(list):
    s=0

    for i in list:
      s +=1
    return s


sum(list)#replaces the above code
