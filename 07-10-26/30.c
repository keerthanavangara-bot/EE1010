// Keerthana
// 7-10-26

#include <stdio.h>

int main() {
    int count = 0;

    // 3^5 = 243 strings; base-3 digits (0=a, 1=b, 2=c)
    for (int i = 0; i < 243; i++) {
        int s[5], n = i;

        // Extract 5 base-3 digits
        for (int j = 4; j >= 0; j--) {
            s[j] = n % 3;
            n /= 3;
        }

        // Check for any two consecutive equal symbols
        int hasDouble = 0;
        for (int j = 0; j < 4; j++) {
            if (s[j] == s[j + 1]) {
                hasDouble = 1;
                break;
            }
        }

        if (hasDouble) count++;
    }

    printf("Strings with at least one double = %d\n", count);

    return 0;
}
