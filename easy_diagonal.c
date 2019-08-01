#include <stdio.h>
#include <string.h>
typedef unsigned long long ull;
ull diagonal(int n, int p) {
  ull result = 0;
  ull pascal[n + 1][n + 1];
  memset(pascal, 0, (n + 1) * (n + 1) * sizeof(ull));
  pascal[0][0] = 1;
  for (int i = 1; i < n + 1; i++) {
    pascal[i][0] = 1;
    for (int j = 1; j < n + 1; j++) {
      pascal[i][j] = pascal[i - 1][j - 1] + pascal[i - 1][j];
    }
  }
  for (int i = p; i < n + 1; i++) {
    result += pascal[i][p];
  }
  return result;
}

int main() {
  printf("%lld\n", diagonal(7, 1));
  printf("%lld\n", diagonal(7, 2));
  return 0;
}
