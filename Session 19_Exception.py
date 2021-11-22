#Error - Program
#amt = 10
#if(amt >20):
    #print("You are eligible to purchase")
#else:
    #print("You are not eligible to purchase")

#----------------------------------------------------#

#Exception - Program
#num = 100
#result = 100/0
#print("The Result is : ",result)

#----------------------------------------------------#

#Try and Except Clause
#a -= [1,2,3]
#try:
    #print("First  Element = %d" %(a[0]))
    #print("Second Element = %d" %(a[1]))
    #print("Fourth Element = %d" %(a[3]))
    
#except:
    #print ("An Error Occured")

#---------------------------------------------------#
 
#Try with Else Clause
#def fun(a,b):
    #try:
        #c = ((a+b)/(a-b))
    #except ZeroDivisionError:
        #print("a/b results in 0")
    #else:
        #print(c)

#fun(2,3)
#fun(3,3)

#--------------------------------------------------#

#Finally Block
#try:
    #k = 10/5
    #k = 5/5

#except ZeroDivisionError:
    #print("Values cannot be divided by zero")
    
#else:
    #print("Else Block Executes")
    #print(k)
    
#finally:
    #print("This Block Always executes")

#-------------------------------------------------#
     
