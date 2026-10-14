#include <stdio.h>

char *my_strcat(char *dest, const char *src) {
    char *temp = dest; // Save the original starting address
    
    while (*dest != '\0') dest++; // Move to the end of the destination string
    while ((*dest++ = *src++) != '\0'); // Copy source characters to the end of destination
    
    return temp; // Return the start of the combined string
}

int main() {
    char dest[50] = "Data";
    char src[] = " Structures";
    
    my_strcat(dest, src);
    
    printf("%s\n", dest); // Output: Data Structures
    return 0;
}

