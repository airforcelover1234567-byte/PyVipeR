list=[3,6,8,1,2,9,7,4,5]

max=list[0]
for i in list:
    if i>max:
        max=i
print("Largest Element: ",max)

min=list[0]
for i in list:
    if min>i:
        min=i
print("Smallest Element: ",min)

total=0
for i in list:
    total+=i
print("Total:",total)
print("Average:",total/2)

for i in list:
    if i%2!=0:
        continue
    print(i)
print("\n")
for i in list:
    if i%2==0:
        continue
    print(i)