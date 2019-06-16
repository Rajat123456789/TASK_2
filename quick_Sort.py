def quick_sort(a,l,h):
    if l<h:
        j= partition (a,l,h)
        quick_sort(a,l,j-1)
        quick_sort(a,j+1,h)
def partition (a,l,h):
    pivot = a[l]
    i=l
    j=h
    while i<j:
        if a[i]<=pivot:
            i=i+1
        if a[j]>pivot:
            j=j-1
        if i<j:
            a[i],a[j]=a[j],a[i]
    a[l],a[j]=a[j],a[l]
    return j

n= int(input("Enter number of elements"))
a=[]
print("Enter the elementss")
for i in range (0,n,1):
    a.append(int(input()))
print("Unsorted array")
print(a)
print("Sorted Array")
quick_sort(a,0,n-1)
print(a)
