#include <stdio.h>
#include <math.h>
#include <string.h>
#include <stdlib.h>
char *factors(int lst)
{
    char *current_str = malloc(100 * sizeof(char));
    char int2string[20];
    int power;
    int current_fac = 2;
    strcpy(current_str, "");
    while (lst != 1)
    {
        power = 0;
        while (lst % current_fac == 0)
        {
            ++power;
            lst /= current_fac;
        }
        if(power == 1)
        {
            sprintf(int2string, "(%d)", current_fac);
            strcat(current_str, int2string);
        }
        else if(power != 0)
        {
            sprintf(int2string, "(%d**%d)", current_fac, power);
            strcat(current_str, int2string);
        }
        ++current_fac;
    }
    // free(current_str);
    return current_str;
}
int main()
{
    printf("%s\n", factors(86240));
    printf("%s\n", factors(7775460));
    printf("%s\n", factors(7919));
    printf("%s\n", factors(17*17*93*677));

}