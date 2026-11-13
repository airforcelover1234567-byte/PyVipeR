names=["Rounak","Sounak","Arya"]
print(names)
for i in range(0,len(names),1):
    print(names[i])

numbers=[2,6,1,9,7]
max=numbers[0]
for number in numbers:
    if number>max:
        max=number
print(max)

total=0
for num in numbers:
    total+=num
print("Total: ",total)
print("Average: ",total/2)

