'''   Zip Function :
                    (1). zip function is used to iterate one or more list having the same length.
                    (2). It Can aslo works with tuple.
'''

l1=[10,60,50,32,10]                 # List 1 :  5 elements
l2=[22,50,32,90,25]                 # List 2 :  5 elements

for a,b in zip(l1,l2):
    print(a,b)                      # Print the 1 by 1 value of both list parallaly

# print the  same element using for loop wih range function logic

print("\n\n With Range function logic:")
t=len(l1)
for h in range(t):
    print(l1[h],l2[h])

