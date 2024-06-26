#include <stdio.h>
int main() {
int a = 0;
int b = 0;
int c = 0;

// Monitored vars =  a
printf("a = %d\n", a)

a = 1;
printf("a = %d\n", a);
b = (a + 5) * (10 + 2);
a = 0;
printf("a = %d\n", a);

return 0;
}