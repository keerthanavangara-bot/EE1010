// Keerthana
// 7-10-26

#include <stdio.h>

int main() {
    int a = 0b1100;   // 12
    int b = 0b1010;   // 10

    // BITWISE &: ANDs each bit separately
    //   1100
    // & 1010
    // ------
    //   1000  = 8
    printf("%d\n", a & b);    // 8

    // LOGICAL &&: both non-zero? -> true
    // 12 is non-zero AND 10 is non-zero -> 1
    printf("%d\n", a && b);   // 1

    return 0;
}
