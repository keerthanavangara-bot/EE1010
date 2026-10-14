#include <stdio.h>
#include <stdlib.h>
#include <math.h>

// --- Data Structures ---
typedef struct sadish {
    double data;
    struct sadish *next;
} sadish;

typedef struct avyuh {
    sadish *vector;
    struct avyuh *next;
} avyuh;

// --- Helper Functions ---
avyuh *createList(int m, int n) {
    avyuh *head = (avyuh *)malloc(sizeof(avyuh));
    avyuh *currMat = head;
    currMat->next = NULL;
    for (int i = 0; i < m; i++) {
        if (i > 0) {
            currMat->next = (avyuh *)malloc(sizeof(avyuh));
            currMat = currMat->next;
            currMat->next = NULL;
        }
        sadish *vecHead = (sadish *)malloc(sizeof(sadish));
        sadish *currVec = vecHead;
        currVec->next = NULL;
        for (int j = 0; j < n; j++) {
            currVec->data = 0.0;
            if (j < n - 1) {
                currVec->next = (sadish *)malloc(sizeof(sadish));
                currVec = currVec->next;
                currVec->next = NULL;
            }
        }
        currMat->vector = vecHead;
    }
    return head;
}

sadish *createVec(int k) {
    sadish *head = (sadish *)malloc(sizeof(sadish));
    sadish *curr = head;
    curr->next = NULL;
    curr->data = 0.0;
    for (int i = 1; i < k; i++) {
        curr->next = (sadish *)malloc(sizeof(sadish));
        curr = curr->next;
        curr->next = NULL;
        curr->data = 0.0;
    }
    return head;
}

sadish *ListVecopy(sadish *a) {
    if (a == NULL) return NULL;
    sadish *head = (sadish *)malloc(sizeof(sadish));
    head->data = a->data;
    head->next = NULL;
    sadish *currNew = head;
    for (sadish *currOld = a->next; currOld != NULL; currOld = currOld->next) {
        currNew->next = (sadish *)malloc(sizeof(sadish));
        currNew = currNew->next;
        currNew->data = currOld->data;
        currNew->next = NULL;
    }
    return head;
}

avyuh *transposeList(avyuh *a) {
    int rows = 0, cols = 0;
    for (avyuh *r = a; r != NULL; r = r->next) rows++;
    if (a != NULL && a->vector != NULL) {
        for (sadish *s = a->vector; s != NULL; s = s->next) cols++;
    }
    avyuh *trans = createList(cols, rows);
    avyuh *tMat = trans;
    for (int j = 0; j < cols; j++) {
        sadish *tVec = tMat->vector;
        avyuh *srcMat = a;
        for (int i = 0; i < rows; i++) {
            sadish *srcVec = srcMat->vector;
            for (int k = 0; k < j; k++) srcVec = srcVec->next;
            tVec->data = srcVec->data;
            tVec = tVec->next;
            srcMat = srcMat->next;
        }
        tMat = tMat->next;
    }
    return trans;
}

avyuh *Listvstack(avyuh *a, avyuh *b) {
    if (a == NULL) return b;
    avyuh *head = (avyuh *)malloc(sizeof(avyuh));
    head->vector = ListVecopy(a->vector);
    head->next = NULL;
    avyuh *curr = head;
    for (avyuh *temp = a->next; temp != NULL; temp = temp->next) {
        curr->next = (avyuh *)malloc(sizeof(avyuh));
        curr = curr->next;
        curr->vector = ListVecopy(temp->vector);
        curr->next = NULL;
    }
    for (avyuh *temp = b; temp != NULL; temp = temp->next) {
        curr->next = (avyuh *)malloc(sizeof(avyuh));
        curr = curr->next;
        curr->vector = ListVecopy(temp->vector);
        curr->next = NULL;
    }
    return head;
}

// --- Include Full Library Functions ---
sadish *ListVecadd(sadish *a, sadish *b){
	sadish *head = (sadish *)malloc(sizeof(sadish)), *c, *tempb=b;
	c = head; 
	head->next = NULL;
	for(sadish *tempa=a;tempa!=NULL;tempa=tempa->next){
        c->data = tempa->data+tempb->data;
        tempb = tempb->next;
        if(tempa->next!=NULL){
            c->next = (sadish *)malloc(sizeof(sadish));
            c->next->next=NULL;
            c= c->next;
        }
	}
	return head;
}

avyuh *Listadd(avyuh *a, avyuh *b){
	avyuh *c= (avyuh *)malloc(sizeof(avyuh)), *tempb = b, *head; 
	c->next = NULL;
	head = c;
	for(avyuh *tempa=a;tempa!=NULL;tempa=tempa->next){
        c->vector = ListVecadd(tempa->vector,tempb->vector);
        tempb = tempb->next;
        if(tempa->next!=NULL){
            c->next = (avyuh *)malloc(sizeof(avyuh));
            c->next->next=NULL;
            c= c->next;
        }
	}
	return head;
}

double ListVecdot(sadish *a, sadish *b){
	double val = 0;
	sadish *tempa=a, *tempb=b;
	while(tempa !=NULL){
		val += tempa->data*tempb->data;
		tempa = tempa->next;
		tempb = tempb->next;
	}
	return val;
}

double Listdot(avyuh *a, avyuh *b){
	return ListVecdot(a->vector, b->vector);
}

double Listdet(avyuh *a){
	double temp1, temp2;	
	temp1 = a->vector->data;
	temp2 = a->vector->next->data;
	a = a->next;
	temp2 = a->vector->data*temp2;
	temp1 = a->vector->next->data*temp1;
	return temp1-temp2;
}

avyuh *rotList(double theta){ 
    avyuh *head = createList(2,2); 
    sadish *row1, *row2;
    double c = cos(theta), s = sin(theta);
    row1 = head->vector;
    row2 = head->next->vector;
    row1->data = c;
    row1->next->data = -s;
    row2->data = s;
    row2->next->data = c;
    return head;
}

// --- Main Testing Driver ---
int main() {
    printf("--- Testing Matrix Operations ---\n");

    // Create 2x2 Matrix A: [1 2; 3 4]
    avyuh *matA = createList(2, 2);
    matA->vector->data = 1.0;
    matA->vector->next->data = 2.0;
    matA->next->vector->data = 3.0;
    matA->next->vector->next->data = 4.0;

    // Test Determinant
    double det = Listdet(matA);
    printf("Determinant of matA: %lf (Expected: -2.00)\n", det);

    // Test Rotation Matrix (theta = 0)
    avyuh *rot = rotList(0.0);
    printf("Rotation Matrix (0 rad) row 1: [%lf, %lf]\n", 
           rot->vector->data, rot->vector->next->data);

    return 0;
}

