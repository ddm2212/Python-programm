#     ***  List Comprehension   ***

'''   1. List Comprehension can use for the Faster execution of data into the list
      2. Variable must br same when you use the comprhenesion and Reduce the line Of Code
'''

# Let's print  value from  1 to 100 with normal methond :
l=[]
for a in range(1,101):
    l.append(a)
print("Normal Method(1 to 100) : \n",l)

# Using the List Comprehension
li=[m for m in range(1,101) if m%2==0]
print("Compresion logic:")
print(li)


 # Converting String into List Using List_Comprehension
name="Dnyaneshwar"
ll=[a for a in name]
print(ll)
