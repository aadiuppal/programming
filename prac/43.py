def maxSubArray(arr):
	prev_max=0
	prev_max_index_start=0
	max_index_end=0
	max_index_start=0
	curr_max=0
	for i in range(0,len(arr)):
		curr_max+=arr[i]
		if prev_max<=curr_max:
			prev_max=curr_max
			prev_max_index_start=max_index_start
			prev_max_index_end=i
		if curr_max<0:
			curr_max=0
			max_index_start=i+1


	return arr[prev_max_index_start:prev_max_index_end+1],prev_max

arr=[1,-3,5,-2,9,-8,-6,4]
print maxSubArray(arr)
