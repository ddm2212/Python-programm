# let's  Undrestand the other function of the list like count,min,max,sort,reverse,index, etc

# lets consider the a simple list,
li=[10,40,27,60,41,52,30,19.10,20,50,10]
strlist= ['Dnyanesh','More','Chhaya','Amruta','Vishal','Manoj']

#  1.Count function()
c=li.count(10)                # this will return the count of total value into list(Works same with list and string
st=strlist.count('More')
print(c,"\t",st)

#  2.Max function()
m=max(li)                       # this will return maximun value into the List
print("This is Max Value: ",m)
strmax=max(strlist)
print("The maxstring in List: ",strmax)       # Return Maximiun String into the List

#  3.Min function
mi=min(li)                                      #this will find min function
print("The Smallest value of list : ",mi)
stmin=min(strlist)
print("The Minimum string into the list : ",stmin)

#  4.Sort Function()
li.sort()
strlist.sort()
print('The Sorted list  is : ',li ," \t", strlist)
# This Will sort the list

#  5.Reverse function
li.reverse()
strlist.reverse()
print("The  Reverse List is ",li,"\n Reverse String List: ",strlist)           # Reversing the Whole List

# 6.Index function
i=li.index(10)               # Return In index Value of 10

print(i)