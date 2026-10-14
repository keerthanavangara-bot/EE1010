#include <stdio.h>
#include <stdlib.h>
#include <math.h>

typedef struct sadish {
    double data;
    struct sadish *next;
} sadish;

typedef struct avyuh {
    sadish *vector;
    struct avyuh *next;
} avyuh;

#include "libs/listfun.h"

int main() {
    // Create a 2x2 Matrix:
    // | 1  2 |
    // | 3  4 |
    avyuh *matA = (avyuh *)malloc(sizeof(avyuh));
    matA->vector = (sadish *)malloc(sizeof(sadish));
    matA->vector->data = 1.0;
    matA->vector->next = (sadish *)malloc(sizeof(sadish));
    matA->vector->next->data = 2.0;
    matA->vector->next->next = NULL;

    matA->next = (avyuh *)malloc(sizeof(avyuh));
    matA->next->vector = (sadish *)malloc(sizeof(sadish));
    matA->next->vector->data = 3.0;
    matA->next->vector->next = (sadish *)malloc(sizeof(sadish));
    matA->next->vector->next->data = 4.0;
    matA->next->vector->next->next = NULL;
    matA->next->next = NULL;

    // Execute Listdet (Expected determinant for this matrix is (1*4) - (2*3) = -2)
    double det = Listdet(matA);

    printf("Determinant: %lf\n", det);

    return 0;
}

