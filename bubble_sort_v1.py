# bubble_sort_v1.py
# https://www.studytonight.com/data-structures/bubble-sort

def bubble_sort(array):
    array_l = len(array);
    for j in range(array_l):
        for i in range(array_l):
            if (i != array_l-1) and (array[i] > array[i+1]):
                temp1 = array[i]
                temp2 = array[i+1]
                array[i] = temp2
                array[i+1] = temp1

    print(array)


def bubble_sort_op(array):
    array_l = len(array);
    flag = 0;
    for j in range(array_l):
        for i in range(array_l):
            if (i != array_l-1) and (array[i] > array[i+1]):
                temp1 = array[i]
                array[i] = array[i+1]
                array[i+1] = temp1
                # flag changes
                flag = 1;
        
        # array is sorted
        if flag == 0:
            break;

    print(array)



if __name__ == "__main__":
    bubble_sort([5, 1, 6, 2, 4, 3])
            