#include <math.h>
#include <stdio.h>
#include <stdlib.h>

long long *gap(int g, long long m, long long n) {
  int last_prime = 0;
  long long *result = malloc(sizeof(long long) * 2);
  result[0] = 0;
  result[1] = 0;
  for (int i = m; i <= n; i++) {
    int is_prime = 1;
    if (i == 2) {
      last_prime = 2;
    } else {
      for (int j = 2; j <= (int)sqrt(i); j++) {
        if (i % j == 0) {
          is_prime = 0;
          break;
        }
      }
      if (is_prime) {
        if (i - last_prime == g) {
          result[0] = (long long)last_prime;
          result[1] = (long long)i;
          return result;
        } else {
          last_prime = i;
        }
      }
    }
  }
  return result;
}

int main() {
  gap(2, 100, 110);
  gap(4, 100, 110);
  gap(6, 100, 110);
  return 0;
}
