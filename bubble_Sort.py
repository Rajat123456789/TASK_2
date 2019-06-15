#BUBBLE SORT
arr=[]
n=int(input("Enter number of elements"))
print("Enter numbers")

for i in range(0,n,1):
    element=int(input())
    arr.append(element)

print("Your array is \n")
print(arr)

print("\n Your array after Bubble Sort is")

for j in range (0,n,1):
    for k in range (n-1):
        if arr[k]>arr[k+1]:
            temp=arr[k]
            arr[k]=arr[k+1]
            arr[k+1]=temp
print("\n")
print(arr)