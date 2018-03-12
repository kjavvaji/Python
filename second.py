a=[1,2,3,4,5,6,7,8,9,10]
i=0
new_list=[]
while i<len(a):
    if a[i]%2==0:
        new_list.append(a[i])
    else:
        new_list.append("#")
    i+=1  # i=i+1
print(new_list)
