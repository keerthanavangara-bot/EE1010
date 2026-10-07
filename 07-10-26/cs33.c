// Keerthana
// 7-10-26

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// fun() from the question — counts swaps
int fun(int A[], int n) {
    int swaps = 0;
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - i - 1; j++) {
            if (A[j] > A[j + 1]) {
                int temp = A[j];
                A[j] = A[j + 1];
                A[j + 1] = temp;
                swaps++;
            }
        }
    }
    return swaps;
}

int main() {
    int n = 30;
    int A[30];

    srand(time(NULL));

    // Generate 30 distinct random integers (0..100)
    for (int i = 0; i < n; i++) {
        int dup;
        do {
            dup = 0;
            A[i] = rand() % 101;
            for (int j = 0; j < i; j++)
                if (A[j] == A[i]) dup = 1;
        } while (dup);
    }

    // Print generated array
    printf("Array A:\n");
    for (int i = 0; i < n; i++) printf("%d ", A[i]);
    printf("\n\n");

    // Just print fun(A)
    printf("fun(A) = %d\n", fun(A, n));

    return 0;
}
