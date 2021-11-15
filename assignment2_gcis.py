#question 1 part a

'importing array and csv'

import array as Array
import csv
with open('assignment2_file.csv','r') as desired_file:
    info=csv.reader(desired_file)
    infolist=[]

    for i in info:
        infolist.append(i)
    tupleinfo=[]

    for i in infolist[1]:
        if i!="":
            tupleinfo.append(int(i))
        else:
            pass
    arrayinfo=list(map(int,infolist[0]))
    tupleinfo=list(map(int,tupleinfo))
    array1=Array.array('i',arrayinfo)
    tuple1=tuple(tupleinfo)
    list1=infolist[2]
    set1=set(infolist[3])
    dict1=dict(zip(infolist[4],infolist[5]))


#question 1 part b 

print(array1,'\n',tuple1,'\n',list1,'\n',set1,'\n',dict1)

with open('assignment2_file.txt','w') as file1:
    data=str(dict1)+'\n'+str(list1)+'\n'+str(tuple1)+'\n'+str(array1)
    file1.write(data)

print("\n")

#question 1 part c

info=[]

with open('assignment2_file.txt','r') as partC:

    for row in partC:
        info.append(row.rstrip())

for i in info:
    print(i)

print("\n")


#question 1 part d


if 'Fujairah' in list1 and 'brown' in set1 and 'Data Science' in dict1:
    print("Found \n 'Fujairah' in list1,\n 'brown' in set1 and \n 'Data Science' in dict1")
else:
    print("nothing found")

print("\n")

#question 2 part a

'array 1 for loop'

for i in range(0,len(array1)):
    digits=array1[i]
    array_func=i-1

    while array_func>=0 and digits<array1[array_func]:
        array1[array_func+1],array1[array_func]=array1[array_func],array1[array_func+1]
        array_func=array_func-1

'tuple1 merge sorting'

def merge_sort(array):

    if len(array)<=1:
        return array

    half=len(array)//2
    L,R=merge_sort(array[:half]),merge_sort(array[half:])
    return merge(L,R)

def merge(L,R):
    result=[]
    L_pointer=R_pointer=0

    while L_pointer< len(L) and R_pointer<len(R):

        if L[L_pointer]<R[R_pointer]:
            result.append(L[L_pointer])
            L_pointer +=1
        else:
            result.append(R[R_pointer])
            R_pointer+=1
    result.extend(L[L_pointer:])
    result.extend(R[R_pointer:])

    return result

tuple1a=list(tuple1)
resultuple1a=merge_sort(tuple1a)
tuple1=tuple(resultuple1a)

'list 1 quick sorting'

def quick_sort(order):
    length = len(order)

    if length < 1:
        return order
    else:
        move = order.pop()

    greaterindex = []
    lowerindex = []

    for index in order:

        if index >move:
            greaterindex.append(index)

        else:
            lowerindex.append(index)

    return quick_sort(lowerindex) + [move] + quick_sort(greaterindex)

quick_sort(list1)


#question 2 part b

'set1 quick sorting'

quick_sort(set1)

'dict1 value sorting'

dict1a={}

for i in sorted(dict1):
    digits=dict1[i]
    dict1a[i]=digits
dict1=dict1a


#question 2 part c

'appending data'

with open('assignment2_file.txt','w') as q2pC:
    data=str(array1)+'\n'+str(tuple1)+'\n'+str(list1)+'\n'+str(set1)+'\n'+str(dict1)
    q2pC.write(data)


#question 2 part d


'reading data'

info=[]

with open('assignment2_file.txt','r') as q2pD:
    for row in q2pD:
        info.append(row.rstrip())

'printing data'

for i in info:
    print(i)

print("\n")

#question 3

'appending sorted data'

with open('assignment2_file2.csv', 'w', encoding='UTF8') as f:
    writer = csv.writer(f)
    
    for i in info:
        digits=[]
        digits.append(i)
        writer.writerow(digits)