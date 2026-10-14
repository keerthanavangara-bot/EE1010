// By Keerthana
// 08-October

#include <stdio.h>
#include <stdlib.h>
#include "libs/listgen.h"

// Function to check if a query value exists in L2
int find(int query, sadish *list) {
    while (list != NULL) {
        if ((int)list->data == query) return 1;
        list = list->next;
    }
    return 0;
}

int main() {
    // Open data files for L1 (9 elements) and L2 (7 elements)
    FILE *fp1 = fopen("L1.dat", "r");
    FILE *fp2 = fopen("L2.dat", "r");

    

    // Load each file into respective sadish vectors
    sadish *v1 = loadVec(fp1, 9);
    sadish *v2 = loadVec(fp2, 7);
    fclose(fp1);
    fclose(fp2);

    // Construct the avyuh matrix structure to hold both vectors
    avyuh *mat = (avyuh *)malloc(sizeof(avyuh));
    mat->vector = v1;
    mat->next = (avyuh *)malloc(sizeof(avyuh));
    mat->next->vector = v2;
    mat->next->next = NULL;

    // Assign L1 and L2 from the avyuh structure
    sadish *L1 = mat->vector;
    sadish *L2 = mat->next->vector;

    
    sadish *ptr1 = L1;
    while (ptr1 != NULL && ptr1->next != NULL) {
        int query = (int)ptr1->next->data;
        if (find(query, L2)) {
            ptr1->next = ptr1->next->next;
        } else {
            ptr1 = ptr1->next;
        }
    }

    // Count and print the final nodes in L1
    int count = 0;
    sadish *curr = L1;
    printf("Modified L1: [ ");
    while (curr != NULL) {
        printf("%d ", (int)curr->data);
        count++;
        curr = curr->next;
    }
    printf("]\n");

    printf("Number of nodes in L1 after execution = %d\n", count);

    return 0;
}

