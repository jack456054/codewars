#include <stdio.h>
#include <string.h>
#include <ctype.h>

char *wave(char *y)
{
  int len = strlen(y);
  int spaces = 0;
  char upper_y[len];
  strcpy(upper_y, y);
  for (int i = 0; i < len; i++)
  {
    if (upper_y[i] == ' ')
    {
      ++spaces;
      continue;
    }
    upper_y[i] = toupper(upper_y[i]);
    printf("%s\n", upper_y);
    upper_y[i] = tolower(upper_y[i - spaces]);
  }
  return 0;
}

int main() {
  printf("%s", wave(" gap "));
  return 0;
}
