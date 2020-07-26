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

def find_k_largest(k, arr):
    if k >= len(arr):
        merge_sort(arr)
        return arr
    # sort array
    merge_sort(arr)
    k_elements = []
    for i in range(k):
        k_elements.append(arr[len(arr) - 1 - i])
    return k_elements




if __name__ == "__main__":
    arr = [2, 3, 20, -1, 100, -5, 5, 10]
    array1 = [94, 12, 1, 564, 2, 4325, 55, 0, -1]
    array2 = [564, 2, 4325]
    print(find_k_largest(3, arr))
    print(find_k_largest(3, array1))
    print(find_k_largest(3, array2))
    
    
