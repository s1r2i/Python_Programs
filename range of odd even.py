print("--------All odd number ranges---------")
n1=int(input("Enter lower range : "))
n2=int(input("Enter upper range : "))
for i in range(n1,n2+1):
    if i%2!=0:
        print(i,end=",")
 
