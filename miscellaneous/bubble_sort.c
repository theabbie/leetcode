#include <stdio.h>

void bubbleSort(int arr[], int n) {
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                int temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }
    }
}

void main() {
    int n;
    int arr[100];
    printf("Size Of Array: ");
    scanf("%d", &n);
    printf("Enter the Array: \n");
    for (int i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
    }
    bubbleSort(arr, n);
    printf("After Sorting: \n");
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
}