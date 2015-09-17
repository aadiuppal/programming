def insertion_sort(arr):
    for i in range(1,len(arr)):
        curr=arr[i]
        pos=i
        while pos>0 and arr[pos-1]>curr:
            arr[pos]=arr[pos-1]
            pos-=1
        arr[pos]=curr
arr=[9,1,5,2,3,-1]
insertion_sort(arr)
print arr
