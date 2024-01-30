#include <stdio.h>

int main() {
    FILE *fp;
    fp = fopen("data.txt", "w");

    if (fp == NULL) {
        printf("Error opening file!\n");
        return 1;
    }

    // Generate x(n) = 20 - n and write to file
    for (int n = 0; n <= 24; ++n) {
        fprintf(fp, "%d %d\n", n, 20 - n);
    }

    fclose(fp);
    return 0;
}
