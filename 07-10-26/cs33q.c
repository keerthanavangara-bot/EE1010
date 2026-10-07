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
                int t = A[j];
                A[j] = A[j + 1];
                A[j + 1] = t;
                swaps++;
            }
        }
    }
    return swaps;
}

int main() {
    int n = 30, A[30];
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

    printf("Array before fun():\n");
    for (int i = 0; i < n; i++) printf("%d ", A[i]);
    printf("\n\n");

    int swaps = fun(A, n);

    printf("Array after fun():\n");
    for (int i = 0; i < n; i++) printf("%d ", A[i]);
    printf("\n\n");

    printf("fun(A) = %d\n", swaps);

    return 0;
}
