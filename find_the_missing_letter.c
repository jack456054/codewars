# include <stdio.h>

char findMissingLetter(char array[], int arrayLength)
{
        int last_char = (int)array[0];
        for(int i = 0; i < arrayLength; i++)
        {
                if ((int)array[i] - last_char >1)
                {
                        return (char)(last_char + 1);
                }
                last_char = (int)array[i];
        }
        return ' ';
}


int main(int argc, char const *argv[]) {
        char arr1[] = { 'a','b','c','d','f' };
        char arr2[] = { 'O','Q','R','S' };
        printf("%c", findMissingLetter(arr1, 5));
        printf("%c", findMissingLetter(arr2, 4));
        return 0;
}
