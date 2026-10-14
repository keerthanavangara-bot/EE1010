#include <stdio.h>
#include <stdlib.h>

typedef struct list {
    double data;
    struct list *next;
} sadish;

sadish *createVec(int n) {
    sadish *head = malloc(sizeof(sadish)), *t = head;
    head->next = NULL;
    for (int i = 0; i < n - 1; i++) {
        t->next = malloc(sizeof(sadish));
        t = t->next;
        t->next = NULL;
    }
    return head;
}

sadish *Vecind(sadish *a, int n) {
    while (n--) a = a->next;
    return a;
}

int main() {
    int n;
    printf("Enter degree n: ");
    scanf("%d", &n);

    sadish *p = createVec(n + 1), *t = p;
    printf("Enter %d coefficients: ", n + 1);
    while (t) { scanf("%lf", &t->data); t = t->next; }

    double a;
    printf("Enter a: ");
    scanf("%lf", &a);

    // (i) Evaluate P(a) via Horner's method
    double val = 0.0;
    for (int i = n; i >= 0; i--) val = val * a + Vecind(p, i)->data;
    printf("P(a) = %.4f\n", val);

    // (ii) Derivative coefficients
    printf("Derivative: ");
    for (int i = 0; i < n; i++) printf("%.2f ", (i + 1) * Vecind(p, i + 1)->data);
    printf("\n");

    return 0;
}

