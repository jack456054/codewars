#include <stdio.h>

int _persistence(int array[2]);
int persistence(int n)
{
    if (n < 10)
    {
        return 0;
    }
    int array[] = {n,
                   0};
    return _persistence(array);
}
int _persistence(int array[2])
{
    int result = 1;
    while (array[0] != 0)
    {
        result *= array[0] % 10;
        array[0] /= 10;
    }
    array[0] = result;
    array[1] += 1;

    if (result < 10)
    {
        return array[1];
    }
    else
    {
        return _persistence(array);
    }
}

int main()
{
    printf("%d", persistence(39));
    printf("%d", persistence(4));
}