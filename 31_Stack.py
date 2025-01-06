
# Stack :  Which Perform( push,pop,front,last,dislay
# we generally perform stack operation of list

l=[]
while True:
    c=int(input(''' Enter The Operation : 
                    1. Push Element
                    2. Pop Element
                    3. Front elemnt
                    4. Last element
                    5. Diplay Element
                    6. Exit   
                
Choose any One Operation from Above: '''))
    if c==1:
        n=int(input("Inset the Element: "))
        l.append(n)
        print(l)
    elif c==2:
        if len(l)==0:
            print("Stak is Empty")
        else:
            p=l.pop()
            print("This element is poped form stack : ",p)
            print(l)
    elif c==3:
        if len(l)==0:
            print("Stak is Empty")
        else:
            print("Front Elemen is : ",l[0])
    elif c==4:
        print("last Elment Of stack:",l[-1])
    elif c==5:
        print("Whole Stack is :",l)
    elif c==6:
         print("Program is Terminated")
         break;

else: print(" Invalid Operation !!!!!!!!!!!!")




