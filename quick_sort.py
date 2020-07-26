# Python program for implementation of quick_sort_aux Sort 

# This function takes last element as pivot, places 
# the pivot element at its correct position in sorted 
# array, and places all smaller (smaller than pivot) 
# to left of pivot and all greater elements to right 
# of pivot 
def partition(arr,low,high): 
	i = ( low-1 )		 # index of smaller element 
	pivot = arr[high]	 # pivot 

	for j in range(low , high): 

		# If current element is smaller than or 
		# equal to pivot 
		if arr[j] <= pivot: 
		
			# increment index of smaller element 
			i = i+1
			arr[i],arr[j] = arr[j],arr[i] 

	arr[i+1],arr[high] = arr[high],arr[i+1] 
	return ( i+1 ) 

# The main function that implements quick_sort_aux 
# arr[] --> Array to be sorted, 
# low --> Starting index, 
# high --> Ending index 

# Function to do Quick sort 
def quick_sort_aux(arr,low,high): 
	if low < high: 

		# pi is partitioning index, arr[p] is now 
		# at right place 
		pi = partition(arr,low,high) 

		# Separately sort elements before 
		# partition and after partition 
		quick_sort_aux(arr, low, pi-1) 
		quick_sort_aux(arr, pi+1, high) 

def quick_sort(arr):
    n = len(arr) 
    quick_sort_aux(arr,0,n-1)    


# This code is contributed by Mohit Kumra 
if __name__ == "__main__":
    # Driver code to test above 
    arr = [10, 7, 8, 9, 1, 5] 
    quick_sort(arr)
    print ("Sorted array is:") 
    for e in arr: 
        print ("%d" %e), 

'''
# Quick Sort 
#
# 
def quick_sort(arr):
    quick_sort_aux(arr, left_e, right_e)


def quick_sort_aux(arr, left_e, right_e):
    if (left_e >= right_e):
        return
    
    # tright in the middle
    pivot = arr[(left_e + right_e)/ 2]

    index = partition(arr,left_e, right_e, pivot)
    quick_sort_aux(arr, left_e, index -1)
    quick_sort_aux(arr, index, right_e)


def partition(arr, left_e, right_e, pivot):
    while(left <= right_e):
        while (arr[left_e] < pivot):
            left_e+=1
        
        while (arr[right_e] < pivot):
            right_e-= 1

        if (left_e <= right_e):
            swap(arr, left_e, right_e)
            left_e +=1 
            right_e-=1

      return left_e
'''