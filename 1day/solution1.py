lists = open('input', 'r')

list1=[]
list2=[]

for line in lists:
    #print(line)
    id1, id2 = line.split()
    id1 = id1.strip()
    id2 = id2.strip()

    #print("id1:",id1)
    #print("id2:",id2)
    list1.append(int(id1))
    list2.append(int(id2))

#print(list1)
#print(list2)    

#sort first list
for j in range(len(list1)-1):
    for i in range(len(list1)-1-j):
        if list1[i]>list1[i+1]:
                temp = list1[i]
                list1[i] = list1[i+1]
                list1[i+1] = temp
for i in range(len(list2)-1):
    for j in range(len(list2)-1-i):
        if list2[j]>list2[j+1]:
            temp = list2[j]
            list2[j] = list2[j+1]
            list2[j+1] = temp

final=0.000
distance=0
for i in range(len(list1)):
    distance=list2[i]-list1[i]
    #print(distance)
    final = final + abs(distance)

print(list1)
print(list2)

print("sum:",final)