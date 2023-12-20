import csv
F=open('contacts.csv','r')
read=csv.reader(F)
L=[]
M=[]
D=[]
for i in read:
    for j in i:
        L.append(j)
    break
numin=L.index('phone')
namein=L.index('first_name')

K=input("Enter num or name :")
if K.isalpha() and len(K)>3:
    for i in read:
        if i[namein]==K:
            for G in i:
                M.append(G)
    D=dict(zip(L,M))
    for i in D:
        print(i,D.get(i))
elif K.isnumeric() and len(K)==10:
    for i in read:
        if i[numin]==K:
            for G in i:
                M.append(G)
    D=dict(zip(L,M))
    for i in D:
        print(i,D.get(i))
else:
    print("Invalid_details")
if len(D)==0:
    print("No database found")



