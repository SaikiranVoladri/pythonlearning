# array is a data structure in which it is a collection of setof same type of elements
from multiprocessing import Array


arr=['sai','kiran','charan','ashok']
print(arr)
print(len(arr))
#pop()function is used to remove the last element from the array and returns the element
arr.pop()
print(arr)
for x in arr:
    print(x)
arr.insert(1,'voladri')
print(arr)
arr.append('abs')
print(arr)
arr.sort()
print(arr)
arr.reverse()
arr.clear()
print(arr)
arr=['sai','kiran','charan','ashok']
print(arr.index('kiran'))





