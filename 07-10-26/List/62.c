#include <stdio.h>
#include <stdlib.h>

// Define LIST datatype as per question 62
typedef struct list {
    int data;
    struct list *next;
} LIST;

// Function to create a linked list from a .dat file
LIST* createListFromFile(const char *filename) {
    FILE *file = fopen(filename, "r");
    if (!file) {
        printf("Error opening file %s\n", filename);
        return NULL;
    }

    LIST *head = NULL, *tail = NULL;
    int val;

    while (fscanf(file, "%d", &val) == 1) {
        LIST *newNode = (LIST *)malloc(sizeof(LIST));
        newNode->data = val;
        newNode->next = NULL;

        if (head == NULL) {
            head = newNode;
            tail = newNode;
        } else {
            tail->next = newNode;
            tail = newNode;
        }
    }

    fclose(file);
    return head;
}

// Function to print a linked list
void printList(const char *name, LIST *head) {
    printf("%s: ", name);
    LIST *curr = head;
    while (curr != NULL) {
        printf("%d -> ", curr->data);
        curr = curr->next;
    }
    printf("NULL\n");
}

// Find function given in the problem
int find(int query, LIST *list) {
    while (list != NULL) {
        if (list->data == query) return 1;
        list = list->next;
    }
    return 0;
}

int main() {
    // Step 1: Create the two vector lists using dat files
    LIST *L1 = createListFromFile("L1.dat");
    LIST *L2 = createListFromFile("L2.dat");

    printf("--- Initial State ---\n");
    printList("L1", L1);
    printList("L2", L2);

    // Step 2: Execute the logic segment from Q.62
    LIST *ptr1 = L1;
    LIST *ptr2 = L2;
    int query;

    while (ptr1->next != NULL) {
        query = ptr1->next->data;
        if (find(query, L2)) {
            ptr1->next = ptr1->next->next;
        } else {
            ptr1 = ptr1->next;
        }
    }

    printf("\n--- After Modification ---\n");
    printList("L1", L1);

    // Step 3: Count final nodes in L1
    int count = 0;
    LIST *curr = L1;
    while (curr != NULL) {
        count++;
        curr = curr->next;
    }
    
    printf("\nNumber of nodes in L1 after execution: %d\n", count);

    return 0;
}

