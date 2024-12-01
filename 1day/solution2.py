lists = open('input', 'r')

list1=[]
list2=[]

for line in lists:
    id1, id2 = line.split()
    id1 = id1.strip()
    id2 = id2.strip()

    list1.append(int(id1))
    list2.append(int(id2))

#sort first list
for j in range(len(list1)-1):
    for i in range(len(list1)-1-j):
        if list1[i]>list1[i+1]:
                temp = list1[i]
                list1[i] = list1[i+1]
                list1[i+1] = temp
#sort second list
for i in range(len(list2)-1):
    for j in range(len(list2)-1-i):
        if list2[j]>list2[j+1]:
            temp = list2[j]
            list2[j] = list2[j+1]
            list2[j+1] = temp

similarity=0
total_similarity=0
for i in range(len(list1)):
    count=0
    for j in range(len(list2)):
        if list1[i]==list2[j]:
            count=count+1
        score=count*list1[i]
    total_similarity=score+total_similarity

print("total:",total_similarity)