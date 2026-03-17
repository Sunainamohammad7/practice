l=[1,2,3,4,5,6,7,8]
a=[i*2 for i in l]
b=[i*2 for i in l if i%2==0]
c=[i for i in l if i%2!=0]
print("This are the numbers that are multiplied by two:", a)
print("This are the numbers that are multiples of two:", b)
