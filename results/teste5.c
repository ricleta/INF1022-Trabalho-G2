#include <stdio.h>
int main() {
int a = 0;
int b = 0;
int c = 0;

// Monitored vars =  c
printf("c = %d\n", c);

a = 10;b = 20;
if (a * b > 150) {
c = a + b;
printf("c = %d\n", c);

} else {
c = a - b;
printf("c = %d\n", c);

};
return 0;
}