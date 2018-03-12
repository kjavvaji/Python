a=[1,2,3,4,5,6,7,8,9,10]
new_list=[]
for number in a:
    if number%2==0:
        new_list.append(number)
    else:
        new_list.append("#")
print(new_list)

