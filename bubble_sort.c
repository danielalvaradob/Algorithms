#include <stdio.h>

// Bubble Sort Algorithm
// Not optimized - O(n)
void bubble_sortNO(int array[], int n) {
    	int i, j, temp;

        for (i = 0; i < n; i ++) {
            for (j = 0; j < n-i-1; j++) {
                if (array[j] > array[j+1]) {
                    // swap elements
                    temp = array[j];
                    array[j] = array[j+1];
                    array[j+1] = temp; 
                }
            }
        } 
        
        printf( "Sorted Array: ");
        for (i = 0; i < n; i++) {
            printf("%d", array[i]);
        }
}




int main() {
    int array1[] = {5, 1, 6, 2, 4, 3};

    bubble_sortNO(array1, 6);
    return 0;
}
