
    #  List  #
'''
        1). This is mutable datatype ( We Can change valu of Variable
        2). list is widely used into python
        3). It can store different Dataype into single Varaible
'''

li=[2212,'dateofbrith',2.4," Dnyaneshwar More"]
li[2]=2000
print(li,type(li))

# Nested List    ---Here this can containg multile list inside the list:
l=[1,3,2,[4,5,6,12,18,14,12,13],(7,9,8)]
print(l[3][0:8:3])           #slcing is used            # [3] for 3rd List element, Then 0 is start of nested list
                                                        #  where 5 is the end of list and 2 is increment of  nested list
ld=[1,2,3,"Hello",[4,5,6]]
print(ld[3])