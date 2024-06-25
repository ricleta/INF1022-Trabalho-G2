#include <stdio.h>
int main() {
int x = 0;
int y = 0;

// Monitored vars =  x
printf("x = %d\n", x)

x = 20;
printf("x = %d\n", x);
for (int i = 0; i < 3; i++) {
y = x * 2;
x = 0;
printf("x = %d\n", x);

};
return 0;
}