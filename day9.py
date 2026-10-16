1#
l=[50,100,600]
l1=[]
for i in l:
    if i<100:
        l1.append('low')
    elif i <300:
        l1.append('medium')
    else:
        l1.append('high')
print(l1)


l=[50,100,600]
l1=['low'if i<100 else 'medium' if i< 300  else 'high' for i in l]
print(l1)


def sales(l):
    l1=['low'if i<100 else 'medium' if i< 300  else 'high' for i in l]
    return l1
print(sales([50,100,600]))

l=[50,100,600]
l1=list(map(lambda i:'low'if i<100 else 'medium' if i< 300  else 'high',l))
print(l1)


2#
marks=[35,60,80]
l1=[]
for i in marks:
    if i<40:
        l1.append('fail')
    elif i <36:
        l1.append('pass')
    else:
        l1.append('distinction')
print(l1)


l=[35,60,80]
l1=list(map(lambda i:'fail' if i<40 else 'pass' if i<36 else 'distinction',l))
print(l1)

l=[35,60,80]
l1= ['fail' if i<40 else 'pass' if i<36 else 'distinction' for i in l]
print(l1)

def marks(l):
    l=[]
    if i<40:
        return 'fail'
    elif i<60:
        return 'pass'
    else:
        return 'distinction'
marks_l=[35,60,80]
l1=list(map(marks,marks_l))
print(l1)

3#
l=[2,-1,0,5]
pos=0
nag=0
zero=0
for i in l:
    if i>0:
        pos+=1
    elif i<0:
        nag+=1
    else:
        zero+=1
print((pos,nag,zero))


4#
l=[10,20,50,90]
count=0
for i in l:
    if i <20 or i >80:
        count+=1
print(count)


5#
l=[100,500,700]
l1=[]
for i in l:
    if i >=500:
        l1.append(i)
print(l1)

6#
l1=[80,70,90]
l2=[80,60,90]
equal_pos_count=0
for i in range(len(l1)):
    if l1[i] == l2[i]:
        equal_pos_count+=1
print(equal_pos_count)



7#
l1=[1,2,3]
l2=[2,3,4]
s=set()
common_id=0
for i in range(len(l1)):
    if  l1[i] in  l2:
        s.add(l1[i])
        common_id+=1
print(s)


8#
l1=[1,2,3]
l2=[2,3,4]
s=set()
for i in range(len(l1)):
    if l2[i] not in l1:
        s.add(l2[i])
print(s)


9#
s={'a':'it','b':'hr','c':'it'}
count=0
target='it'
for i in s.values():
    if i == target:
        count+=1
print(count)

10#
d={'a':40000,'b':60000,'c':50000}
res={}
for k,v in d.items():
    if v >=50000:
        res[k]=v
print(res)


11#
d={'a':2,'b':5,'c':8}
even_count=0
for i in d.values():
    if i%2==0:
        even_count+=1
print(even_count)


12#
d={'a':2,'b':8}
for i in d:
    if d[i] <5:
        d[i]=5
print(d)


13#
t1=(5,2,8)
t2=(3,4,8)
count_pos=0
for i in range(len(t1)):
    if  t1[i]> t2[i]:
        count_pos+=1
print(count_pos)

14#
t=(10,12,15,21)
l=[]
for i in t:
    if i%5==0:
        l.append(i)
print(l)


15#
s1={'a','b','c'}
s2={'a','b'}
if s1.issubset(s2):
    print('complete')
else:
    print('incomplete')


16#
s1={1,2,3}
s2={4,5}
if len(s1)>len(s2):
    print('larger first')
else:
    print('imcomplete')

17#
l=[50,100,250,600]
l1=[]
for i in l:
    if i>=100 and i<500:
        l1.append(i)
print(l1)

18#
l=[100,200,1200,300]
l1=[]
for i in l:
    if i>1000:
        break
    l1.append(i)
print(l1)


19#

l = [10, -1, 20] 
total = 0
for i in l:
    if i != -1:  
        total += i
print(total) 

20#
l = [35, 40, 80, 105]  
count = 0
for i in l:
    if i >= 40 and i <= 100:  
        count += 1

print(count)





