def magic_index(arr,start,end):
	if start>end:
		return 
	mid=(start+end)/2
	if arr[mid]==mid:
		return mid
	if not magic_index(arr,start,mid-1):
		return magic_index(arr,start,mid-1)
	return magic_index(arr,mid+1,end)

print magic_index([1,2,2,5],0,3)
