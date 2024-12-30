
 #list iteration
print("***    List Iteration   ***")
l=[10,20,30,40,50,60,70,80,90]
lol=len(l)
print(lol)

# (1)  1st method of iteration
for a in range (lol):
     print(l[a])

# (2) Second Method Of Iteration using in keyword
for n in l:
    print(n)

# (3) Reversing  the list using range function   '''
print("\n   Reverse list using range")
for a in range(lol-1,-1,-1):
    print(l[a])
print("End of Range Exectuion")

# (4) Reversing the List using in  keyword
print("\n Reverse using  keyword")
for n in l[-5::-1]:
    print(n)