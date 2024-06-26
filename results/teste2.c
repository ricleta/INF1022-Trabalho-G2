#include <stdio.h>
int main() {
int a = 0;
int b = 0;

// Monitored vars =  b
printf("b = %d\n", b);

a = 15;
if (a > 10) {
b = a - 10;
printf("b = %d\n", b);

} else {
b = a + 10;
printf("b = %d\n", b);

};
return 0;
}