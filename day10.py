marks=[35,40,70]
l=[]
for i in marks:
    if i >=40:
        l.append("pass")
    else:
        l.append("fail")
print(l)

l=[100,200,300]
target=200
l1=[]
for i in l:
    if i <=target:
        l1.append("bellow target")
    else:
        l1.append("above traget")
print(l1)

attendance=[80,70,75]
l=[]
for i in attendance:
    if i >=75:
        l.append("eligible")
    else:
        l.append("shortage")
print(l)

price=[400,600,800]
l=[]
for i in price:
    if i >500:
       l.append(i-10)
    else:
        l.append(i)
print(l)


l1=[80,60,90]
l2=[70,55,75]
count=0
for i in range(len(l1)):
    if abs(l1[i]-l2[i])>=10:
        count+=1
print(count)


l=[1,2,1]
l1=[]
for i in l:
    if i  in l1:
       print("duplicate found")
    else:
       l1.append(i)


l1=[1,2,3]
l2=[2,3,4]
common_set=set()
for i in l1:
    if i in l2:
        common_set.add(i)
print(common_set)

l1=[1,2,3]
l2=[3,4]
pro_id=set()
for i in l1:
    if i not in l2:
        pro_id.add(i)
for i in l2:
    if i not in l1:
        pro_id.add(i)
print(pro_id)

d={'a':'it','b':'hr','c':'it'}
d1={}
for k,v in d.items():
    if k in d1:
        d1[v]+=1
    else:
        d1[v]=1
print(d1)


d=['a','b','c','a']
d1={}
for i in d:
    if i in d1:
        d1[i]+=1
    else:
        d1[i]=1
print(d1)

d={'a':2,'b':5,'c':3}
highest_frequency=0
highest_key=' '
for i in d:
    if d[i]>highest_frequency:
        highest_frequency=d[i]
        highest_key=i
        
print(highest_key)


d={'a':3,'b':8,'c':1}
d1={}
for v in d:
    if d[v] <5:
        d1[v]=[v]
print(list(d1))

d={('pen',20),('book',50)}
d1={}
for i in d:
    d1.update(d)
print(d1)

d={'a':40000,'b':60000,'c':50000}
l=[]
for i in d:
    if d[i] >=50000:
        l.append(i)
print(l)

d={'a','b','c'}
d1=['a','b']
for i in d:
    if i in d1:
        print("present")
        break
    else:
        print("not present")

l=[('a',100),('b',50),('a',200)]
sum=0
for i in l:
    if i[0]=='a':
        sum+=i[1]
print(sum)


l=[50,70,80]
s=65
count=0
for i in l:
    if i>=s:
        count+=1
print(count)


l=[50,100,250,600]
sum=0
for i in l:
    if i>=100 and i<=500:
        sum+=i
print(sum)


l=[('pen',10),('book',3),('bag',2)]
for i in l:
    if i[1]< 5:
        res=i[0]
        break
print(res)


d={'a':3,'b':5,'c':8}
s=set()
for k,v in d.items():
    if v >=5:
        s.add(k)
print(s)

