i=int(input("Please enter a number: "))
l=[]
for x in range (2, i):
    n = i
    if n % x == 0:
        l = l + x
