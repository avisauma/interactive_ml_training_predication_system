
def marks(l):
    s=[]
    for i in l:
        if i >=40:
            s.append(i) 
    return s
print(marks([35,40,75]))


def count(l):
    count=0
    for i in l:
        if i>500:
            count+=1
    return count
print(count([200,600,700]))

def count(l):
    count=0
    for i in l:
        if i <5:
            count+=1
    return count
print(count([2,8,4]))


def sum(l):
    sum=0
    for i in l:
        if i > 0:
            sum+=i
    return sum
print(sum([100,-20,50]))


def target(l):
    target=18
    count=0
    for i in l:
        if i == target:
            count+=1
            break
    return count
print(target([12,18,25])) 

def count(l):
    count=0
    for i in l:
        if len(i)>=5:
            count+=1
    return count
print(count(['ravi','anita','kiran']))


def prices(l):
    l1=[]
    for i in l:
        if i >=500:
            l1.append(i)
    return l1
print(prices([100,500,700]))


def even_sum(l):
    even_sum=0
    for i in l:
        if i % 2==0:
            even_sum+=i
    return even_sum
print(even_sum([101,200,302]))


def count(l):
    count=0
    target='food'
    for i in l:
        if i ==target:
            count+=1
    return count
print(count(['food','tech','food']))

def highest_position(l):
    max_val=l[0]
    max_pos=0
    for i in range(len(l)):
        if l[i]>max_val:
            max_val=l[i]
            max_pos=i
    return max_pos
print( highest_position([[5,8,3],[4,9,2]]))



def marks(l):
    l1=[]
    for i in l:
        if i >=40:
            l1.append(i)
    return l1
print(marks([35,40,70]))


def count(l):
    count=0
    for i in l:
       if i >=15:
           count+=1
    return count
print(count([10,20,30]))


def intersection(l):
    return l[0]&l[1]

print(intersection([{'a','b'},{'b','c'}]))


def difference(l):
    return l[1]-l[0]
print(difference([{'a','b'},{'b','c'}]))



def count(l):
    unique=[]
    count=0
    for i in l:
        if i not in unique:
            unique.append(i)
            count+=1
    return count
print(count(['south','north','south','east']))


def ages(l):
    l1=[]
    for i in l:
        if i>=18:
            l1.append(i)
    return l1
print(ages([15,18,21]))


def sum_price(l):
    sum_price=0
    for i in l.values():
        sum_price+=i
    return sum_price
print(sum_price({'pen':10,'book':5,'bag':2}))


