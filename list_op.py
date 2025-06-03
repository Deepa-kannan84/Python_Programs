list1 = [10, 30, 40, 30, 10]
for i in range(len(list1)):
    if list1[i] == 30:
        list1[i] = 3500
print(list1)
# getting index value by its value

n = 10
print('Iterating list by its value to get first occurrence only')
for v in list1:
    if v == n:
        index1 = list1.index(v)
        print('index of 10 is:',index1)
print('Iterating list by its index to get all the occurrences')
for i in range(len(list1)):
    if n == list1[i]:
        print('index of 10 is:',i)
print('Using index method to get first occurrence only')
print(list1.index(n))
