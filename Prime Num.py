a=int(input("Enter Number:"))
#print(a)
if (a==1):
   print("1 is a whole number")
else:
    for i in range(2,a+1):
        j=0
        for k in range(2,i//2+1):
            if(i%k==0):
                j+=1
        if(j<=0):
            print(i)
