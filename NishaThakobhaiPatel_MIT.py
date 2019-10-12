no=int(input("Enter Number between 0 to 100 : "))
lst=[]
i=1
while i<=no:
     count=0
     if(no%i==0):
          j=1
          while(j<=i):
               if(i%j==0):
                    count=count+1
               j=j+1
          if(count==2):
               lst.append(i)
     i=i+1
     
print("Prime Fectors : ")
print(lst)
     

     
