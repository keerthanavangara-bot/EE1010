#include <stdio.h>
#include <stdlib.h>
#include <math.h>

// Define custom linked-list structures
typedef struct sadish {
    double data;
    struct sadish *next;
} sadish;

typedef struct avyuh {
    sadish *vector;
    struct avyuh *next;
} avyuh;

// Include the header from the libs folder
#include "listfun.h"

int main() {
    // Create Matrix A: [1 2]
    avyuh *matA = (avyuh *)malloc(sizeof(avyuh));
    matA->vector = (sadish *)malloc(sizeof(sadish));
    matA->vector->data = 1.0;
    matA->vector->next = (sadish *)malloc(sizeof(sadish));
    matA->vector->next->data = 2.0;
    matA->vector->next->next = NULL;
    matA->next = NULL;

    // Create Matrix B: [3 4]
    avyuh *matB = (avyuh *)malloc(sizeof(avyuh));
    matB->vector = (sadish *)malloc(sizeof(sadish));
    matB->vector->data = 3.0;
    matB->vector->next = (sadish *)malloc(sizeof(sadish));
    matB->vector->next->data = 4.0;
    matB->vector->next->next = NULL;
    matB->next = NULL;

    // Test Listadd function
    avyuh *result = Listadd(matA, matB);

    printf("Result of Listadd: [%lf, %lf]\n", result->vector->data, result->vector->next->data);

    return 0;
}

