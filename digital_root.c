#include <stdio.h>

int digital_root(int n)
{
    int result = 0;
    int remain = 0;
    printf("Hello\n");
    printf("%d\n", n);
    while (n != 0)
    {
        remain = n % 10;
        n /= 10;
        result += remain;
    }
    printf("%d", result);
    if (result < 10)
    {
        return result;
    }
    else
    {
        return digital_root(result);
    }
}

int main()
{
    int target = 942;
    int ans = digital_root(942);
    printf("%d", ans);
}