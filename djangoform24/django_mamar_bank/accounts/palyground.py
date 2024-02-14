
# a = 3
# try:
#     n = 4/0
# except a==3 :n=5
# print(n)



# def fun(*args , **kwargs):
     
#      if(kwargs):print(kwargs)



# fun((54,5,6,7),6,{'a':4})


def myFun( **kwargs):
   print(kwargs)
 
 
# Driver code
myFun( first='Geeks', mid='for', last='Geeks')