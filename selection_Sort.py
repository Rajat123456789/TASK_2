#Selection SORT
a=[]
n=int(input("Enter number of elements"))
print("Enter numbers")

for i in range(0,n,1):
    element=int(input())
    a.append(element)

print("Your array is \n")
print(a)

print("\n Your array after Selection Sort is")

for p in range (0,n,1):
    min=p
    for q in range (p,n,1):
        if a[min]>a[q]:
            temp=a[q]
            a[q]=a[min]
            a[min]=temp


print(a)
