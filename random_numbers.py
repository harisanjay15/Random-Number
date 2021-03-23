l=[]
m=99999
x=1
a=33334 
c=57527


def check(l):
    cout=0
    print("checking unique........")
    flag=1
    for i in range(len(l)):
        ccc=0
        for i1 in range(len(l)): 
            ccc=c+1
            if i != i1: 
                if l[i] == l[i1]: 
                    cout =cout+1
                    if(flag==1):
                        print(ccc)
                    flag = 0
    print(cout)
    return flag

def checker(l):
    flag=1
    for i in range(1,m):
        occ=l.count(i)
        if(occ != 1 and occ !=0):
            print(str(i)+" -- "+str(occ))
            flag=0
    return flag



for i in range(0,99999):
   
    value=(((a*x)+c)%m)
    
    x=value
   
    l.append(x)
print("generating random numbers........")

print(l)

print(len(l))

with open('file.txt', 'w') as file:
    for item in l:
        file.write('%s\n' % item)

if(check(l)):
    print("unique")
else:
    print("not unique")