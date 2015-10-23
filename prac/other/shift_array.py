def shift_array(arr,k):
    reverse(arr,0,len(arr)-1-k)
    reverse(arr,len(arr)-k,len(arr)-1)
    reverse(arr,0,len(arr)-1)
def reverse(arr,i,j):
    while i < j:
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp
        i += 1
        j -= 1
arr = [1,2,3,4,5,6,7]
shift_array(arr,3)
print arr
