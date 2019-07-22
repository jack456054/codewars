#include <stdio.h>
#include <math.h>
int digPow(int n, int p)
{
    // int n_power = pow(n, p);
    // int power_sum = 0;
    // int length = 0;
    // int current_num = n;
    // while (current_num != 0)
    // {
    //     ++length;
    //     current_num /= 10;
    // }
    // current_num = n;
    // for (int i = p + length - 1; i >= p; i--)
    // {
    //     power_sum += pow(current_num % 10, i);
    //     current_num /= 10;
    // }
    // return power_sum % n != 0 ? -1 : power_sum / n;

    // Better version:
    int length = ceil(log10(n));
    int power_sum = 0;
    int current_num = n;
    for (int i = p + length - 1; i >= p; i--)
    {
        power_sum += pow(current_num % 10, i);
        current_num /= 10;
        printf("%d, %d\n", i, power_sum);
    }
    return power_sum % n != 0 ? -1 : power_sum / n;
}

int main()
{
    printf("%d", digPow(695, 2));
}
