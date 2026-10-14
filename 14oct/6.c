#include <stdio.h>


typedef struct {
    int n;          
    double a[21];   
} Polynomial;

// Horner's method for fast O(n) evaluation of P(x)
double evaluate(Polynomial p, double x) {
    double res = 0.0;
    for (int i = p.n; i >= 0; i--) {
        res = res * x + p.a[i];
    }
    return res;
}

// Compute the derivative polynomial
Polynomial derivative(Polynomial p) {
    Polynomial d;
    if (p.n == 0) {
        d.n = 0;
        d.a[0] = 0.0;
        return d;
    }
    
    d.n = p.n - 1;
    for (int i = 0; i <= d.n; i++) {
        d.a[i] = (i + 1) * p.a[i + 1]; // Power rule
    }
    return d;
}

int main() {
    Polynomial p;
    
    printf("Enter degree n (<= 20): ");
    scanf("%d", &p.n);
    
    printf("Enter %d coefficients (a0 to an):\n", p.n + 1);
    for (int i = 0; i <= p.n; i++) {
        scanf("%lf", &p.a[i]);
    }
    
    double a;
    printf("Enter floating-point number a: ");
    scanf("%lf", &a);
    
    
    printf("(i) P(a) = %.4f\n", evaluate(p, a));
    
    
    Polynomial d = derivative(p);
    printf("(ii) Derivative coefficients: ");
    for (int i = 0; i <= d.n; i++) {
        printf("%.2f ", d.a[i]);
    }
    printf("\n");
    
    return 0;
}

