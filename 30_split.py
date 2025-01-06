
#  Dividing the string of user input using splict Function()

l=input(print("enter the Value "))
n=l.split()
print(n)

# Without using Split function 

li=[]
for a in range(1,5):
   n=input("enter the Value "+str(a)+":-")
   li.append(n)
print(li)


''' OUTPUT:- 

enter the Value 
Dnyaneshwar Dilip More
['Dnyaneshwar', 'Dilip', 'More']

enter the Value 1:-Rohit
enter the Value 2:-Balu
enter the Value 3:-badhe
enter the Value 4:-BG
['Rohit', 'Balu', 'badhe', 'BG']

Process finished with exit code 0    '''