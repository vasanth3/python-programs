def sumsquare(l):

   odd=0

   even=0

   for i in l:

       if i%2==0:

           even = even + i**2

       else:

           odd = odd + i**2

   l=[odd,even]

   return(l)


s=int(input("enter the terms"))
l=[]
for i in range(0,s):
   o=int(input())
   l.append(o)
print(l)
print(sumsquare(l))
