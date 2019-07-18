#include <stdio.h>
int nbYear(int p0, double percent, int aug, int p)
{
    int years = 0;
    while (p0 < p)
    {
        p0 += p0 * (percent / 100) + aug;
        years += 1;
    }
    return years;
}

int main()
{
    printf("%d", nbYear(1500000, 2.5, 10000, 2000000));
}