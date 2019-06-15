#Insertion SORT
a=[]
n=int(input("Enter number of elements"))
print("Enter numbers")

for i in range(0,n,1):
    element=int(input())
    a.append(element)

print("Your array is \n")
print(a)

print("\n Your array after Insertion Sort is")

for i in range (0,n,1):
    temp=a[i]
    p=i

    while p>0 and a[p-1]>temp:
        a[p]=a[p-1]
        p=p-1
    a[p]=temp

print(a)
