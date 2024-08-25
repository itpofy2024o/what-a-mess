import pandas as pd
import math

df = pd.read_csv("his.csv").iloc[:,1:]

def reduce(n):
    while len(str(n))>1:
        f = str(n)
        g = 0
        for h in f:
            g+=int(h)
        n=g
    return n

r1r,r2r,r3r,r4r=[],[],[],[]

for i in range(len(df)):
    r1 = df.iloc[i,0].split(",")
    r1[0] = r1[0][1:]
    r1[-1] = r1[-1][:-1]
    r1 = [e.strip() for e in r1]
    df.iloc[i,0]=[int(q) for q in r1]
    r2 = df.iloc[i,1].split(",")
    r2[0] = r2[0][1:]
    r2[-1] = r2[-1][:-1]
    r2 = [e.strip() for e in r2]
    df.iloc[i,1]=[int(q) for q in r2]
    r3 = df.iloc[i,2].split(",")
    r3[0] = r3[0][1:]
    r3[-1] = r3[-1][:-1]
    r3 = [e.strip() for e in r3]
    df.iloc[i,2]=[int(q) for q in r3]
    r4 = df.iloc[i,3].split(",")
    r4[0] = r4[0][1:]
    r4[-1] = r4[-1][:-1]
    r4 = [e.strip() for e in r4]
    df.iloc[i,3]=[int(q) for q in r4]
    rr1,rr2,rr3,rr4=[],[],[],[]
    for k in r1:
        k=int(reduce(k))
        rr1.append(k)
    for k in r2:
        k=int(reduce(k))
        rr2.append(k)
    for k in r3:
        k=int(reduce(k))
        rr3.append(k)
    for k in r4:
        k=int(reduce(k))
        rr4.append(k)
    r1r.append(rr1)
    r2r.append(rr2)
    r3r.append(rr3)
    r4r.append(rr4)

df["r1r"]=r1r
df["r2r"]=r2r
df["r3r"]=r3r
df["r4r"]=r4r

ansr = []

def sec(n,k):
    check = False
    w = 0
    for p,y in enumerate(n):
        if y == k:
            if check == True:
                w = p
                break
            check = True
    return w

for p in range(len(df)):
    ans=df["ans"][p]
    a=ans.split(",")
    a[0]=a[0][1:]
    a[-1]=a[-1][:-1]
    a=[int(h.strip()) for h in a]
    ans=a
    r=[]
    for k in ans:
        r.append(reduce(k))
    ansr.append(r)

df["ansr"]=ansr

note=[]
    
for j in range(len(df)):
    r1r=df["r1r"][j]
    r2r=df["r2r"][j]
    r3r=df["r3r"][j]
    r4r=df["r4r"][j]
    r1=df["r1"][j]
    r2=df["r2"][j]
    r3=df["r3"][j]
    r4=df["r4"][j]
    uni=[]
    for i in r1r:
        if i not in uni:
            uni.append(i)
    for i in r2r:
        if i not in uni:
            uni.append(i)
    for i in r3r:
        if i not in uni:
            uni.append(i)
    for i in r4r:
        if i not in uni:
            uni.append(i)
    elseuni=[]
    for i in range(1,10):
        if i not in uni:
            elseuni.append(reduce(i))
    same=[]
    for i in r1:
        if i in r2 or i in r3 or i in r4:
            same.append(reduce(i))
    for i in r2:
        if i in r1 or i in r3 or i in r4:
            same.append(reduce(i))
    for i in r3:
        if i in r2 or i in r1 or i in r4:
            same.append(reduce(i))
    for i in r4:
        if i in r2 or i in r3 or i in r1:
            same.append(reduce(i))
    same=list(set(same))
    sameloca=[]
    for w in range(len(r4r)):
        if w != len(r4r)-1:
            if r4r[w]==r4r[w+1]:
                if r3r[w]==r4r[w] or r3r[w+1]==r4r[w+1]:
                    sameloca.append(r4r[w])
    three=[]
    for k in range(1,10):
        if r1r.count(k)+r2r.count(k)+r3r.count(k)+r4r.count(k)==3:
            three.append(k)
    threearea = []
    for v in three:
        loc = []
        if r1r.count(v) == 1:
            loc.append([r1r.index(v)+1,4])
        elif r1r.count(v) == 2:
            loc.append([r1r.index(v)+1,4])
            z=sec(r1r,v)
            loc.append([z+1,4])
        
        if r2r.count(v) == 1:
            loc.append([r2r.index(v)+1,3])
        elif r2r.count(v) == 2:
            loc.append([r2r.index(v)+1,3])
            z=sec(r2r,v)
            loc.append([z+1,3])

        if r3r.count(v) == 1:
            loc.append([r3r.index(v)+1,2])
        elif r3r.count(v) == 2:
            loc.append([r3r.index(v)+1,2])
            z=sec(r3r,v)
            loc.append([z+1,2])

        if r4r.count(v) == 1:
            loc.append([r4r.index(v)+1,1])
            print(loc,v)
        elif r4r.count(v) == 2:
            loc.append([r4r.index(v)+1,1])
            z=sec(r4r,v)
            loc.append([z+1,1])
    sasa=[]
    for i in same:
        sasa.append(i)
    for i in sameloca:
        sasa.append(i)
    for i in elseuni:
        sasa.append(i)
    sasa=list(set(sasa))
    note.append(sasa)

df["outcats"]=note
print(df.tail())

print([k for k in range(1,10) if k not in df.iloc[-1,-1]])

print(df.iloc[-1,5])

print(df.iloc[-1,6])

print(df.iloc[-1,7])

print(df.iloc[-1,8])