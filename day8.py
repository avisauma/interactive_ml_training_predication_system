marks=[35,40,75]
l=[]
for i in marks:
    if i >=40:
        l.append(i)
print(l)

l=[200,600,700]
count=0
for i in l:
    if i>500:
        count+=1
print(count)


l=[2,8,4]
count=0
for i in l:
    if i <5:
        count+=1
print(count)


num=[100,-20,50]
sum=0
for i in num:
    if i > 0:
        sum+=i
print(sum)

l=[12,18,25]
target=18
for i in l:
    if i == target:
        print(1)
        break

s=['ravi','anita','kiran']
count=0
for i in s:
    if len(i)>=5:
        count+=1
print(count)

s=[100,500,700]
l=[]
for i in s:
    if i >=500:
        l.append(i)
print(l)


l=[101,200,302]
even_sum=0
for i in l:
    if i % 2==0:
        even_sum+=i
print(even_sum)

l=['food','tech','food']
count=0
target='food'
for i in l:
    if i == target:
        count+=1
print(count)


s1=[5,8,3]
s2=[4,9,2]
max_val=l[0]
max_pos=0
for i in range(len(l)):
    if l[i]>max_val:
        max_val=l[i]
        max_pos=i
print(max_val)


marks=(35,40,70)
l=[]
for i in marks:
    if i >=40:
        l.append(i)
print(l)

l=(10,20,30)
count=0
for i in l:
    if i >=15:
        count+=1
print(count)


s1={'a','b'}
s2={'b','c'}
print(s1.intersection(s2))


s1={'a','b'}
s2={'b','c'}
print(s2.difference(s1))

l=['south','north','south','east']
unique=[]
count=0
for i in l:
    if i not in unique:
        unique.append(i)
        count+=1
print(count)

l=[15,18,21]
l1=[]
for i in l:
    if i>=18:
        l1.append(i)
print(l1)



l={'pen':10,'book':5,'bag':2}
sum_price=0
for i in l.values():
    sum_price+=i
print(sum_price)

