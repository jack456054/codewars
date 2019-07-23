#include <stdio.h>
#include <math.h>
typedef struct Pair Pair;
struct Pair {
    long long first;
    long long snd;
};
// fill length with the number of pairs in your array of pairs
Pair** listSquared(long long m, long long n, int* length) {
    struct Pair **pairs = malloc(10 * sizeof(struct Pair*));
    double square_sum = 0;
    double sqrt_square_sum = 0;
    int current_fac_size = 0;
    for(int num = m; num <= n; num++)
    {
        square_sum = 0;
        sqrt_square_sum = 0;
        for(int i = 1; i <= num; i++)
        {
            if (num % i == 0)
            {
                square_sum += pow(i, 2);
            }
        }
        sqrt_square_sum = sqrt(square_sum);
        if (sqrt_square_sum == (int)sqrt_square_sum)
        {
            pairs[current_fac_size] = malloc(sizeof(Pair));
            (*pairs[current_fac_size]).first = num;
            (*pairs[current_fac_size]).snd = square_sum; 
            ++current_fac_size;
        }
    }
    *length = current_fac_size;
    return pairs;
}