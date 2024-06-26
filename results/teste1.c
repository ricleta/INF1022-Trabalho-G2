#include <stdio.h>
int main() {
int x = 0;
int y = 0;

// Monitored vars =  x
printf("x = %d\n", x);

x = 10;
printf("x = %d\n", x);
y = 2 * x + 5;
return 0;
}