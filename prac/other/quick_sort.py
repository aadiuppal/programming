def quicksort(arr,l,h):
    print arr[l:h+1]
    if l<h:
        p=partition(arr,l,h)
        print arr
        quicksort(arr,l,p-1)
        quicksort(arr,p+1,h)
def partition(arr,l,h):
    pivot=arr[h]
    i=l
    for j in range(l,h):
        if arr[j]<=pivot:
            temp=arr[j]
            arr[j]=arr[i]
            arr[i]=temp
            i+=1
    temp=arr[i]
    arr[i]=arr[h]
    arr[h]=temp
    return i
s=[10,1,6,2,5,3]
quicksort(s,0,len(s)-1)
print s
