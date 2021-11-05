a=int(input())
ctr=0
for i in range(2,a):
    if a%i==0:
        ctr=ctr+1
        break
    if ctr==0:
        print("prime")
    else:
        print("not prime")