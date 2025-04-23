/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* transformArray(int* nums, int numsSize, int* returnSize) {
    *returnSize = numsSize;
    int evencount = 0, oddcount = 0;
    int* arr = malloc(numsSize * sizeof(int));
    for (int i = 0; i < numsSize; i++) {
        if (nums[i] % 2 == 0){
            evencount++;
        } else {
            oddcount++;
        }
    }
    for (int i = 0; i < evencount; i++) {
        arr[i] = 0;
    }
    for (int i = evencount; i < numsSize; i++) {
        arr[i] = 1;
    }
    for (int i = 0; i < numsSize - 1; i++) {
        int temp;
        for (int j = 0; j < numsSize - i - 1;j++) {
        if(arr[j] > arr[j+1]) {
            temp = arr[j];
            arr[j] = arr[j+1];
            arr[j+1] = temp;
        }
        }
        }
    return arr;
    }