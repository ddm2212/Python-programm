
# List Function :
'''         (1). Pop() function:
                    --  pop() works on indexing.
                    --   this Will Retunr the Deleted Value.

'''
l=[1,2,3,4,5,6,7,8,9,10]
l.pop(2)
print(l.pop(4))
print(l)

'''            (2). Del() Function:
                    -- del() works on indexing.  # syntax: del l[x]  ; where x is index number
                    -- if  you delete somthing using del , no value will be return as Ack.
                    -- Only used for List[]
'''
del l[0]
print(l)

'''            (3). Remove Function:
                    -- This will works on  Value .
                    -- Does not Return Value.
'''
l.remove(5)
print(l)
'''             (4). Clear Fucntion:
                    -- Clear Whole the list
'''
l.clear()
print(l)


# (1) Update List_Function:

l=[20,30,40,50,60,70]
print("\n\n Update ListFunction:\n current List:",l)
print("Trying to Insert 80 elemet at index position 4 ")
l[4]=80             # Updating the Value of 60 to  80
print("Updated list:",l)

# (2) Insert List_Fun():
l.insert(0,10)
print("Inserted List element",l)

# (3) Append List_fun():
print("\n Append_list",l)
l.append(90)            # you also append another list string into exesting list.
d=[1,2,3,4,5]
l.append(d)
print(l)

# (4)  Extend List_fun:
ll=["dnyaneshwar",100,35,60]
l.extend(ll)
print(l)
