#Count even and odd numbers in a array
a=[1,2,3,4,5,10,12,13,56]
even=0
odd=0
for i in range (len(a)):
    if(a[i]%2==0):
        even+=1
    else:
        odd+=1
print(f"Even numbers are :{even} and odd numbers are :{odd}")            