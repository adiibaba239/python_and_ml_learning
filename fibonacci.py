print("program for printing fibonacci sum")
sum=2
e1=0
e2=2
e3=0
n=4000000
while e3<n:
    e3 = 4 * e2 + e1
    print(e3,e2,e1)
    sum+=e3
    e1=e2
    e2=e3
sum=sum -e3
print("sum:",sum)