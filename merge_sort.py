def merge_sort(arr):
    # if it's 1 then it is the base case
    if len(arr) > 1:
        mid = len(arr)//2 # get the middle index
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0
    
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i+=1
            
            else:   #if right half element is smaller
                arr[k] = right_half[j]
                j+=1
            k+=1
        
        # if there are values left on either list
        while i < len(left_half):
            arr[k] = left_half[i]
            k+=1
            i+=1
        
        while j < len(right_half):
            arr[k] = right_half[j]
            k+=1
            j+=1

if __name__ == "__main__":
    array1 = [94, 12, 1, 564, 2, 4325, 55, 0, -1]
    print("Given array is:", array1)
    merge_sort(array1)
    print("Sorted array: ", array1)
        