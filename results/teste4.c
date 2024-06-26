#include <stdio.h>
int main() {
int x = 0;
int y = 0;

// Monitored vars =  y x
printf("y = %d\n", y);
printf("x = %d\n", x);

x = 20;
printf("x = %d\n", x);
for (int i = 0; i < 3; i++) {
y = x * 2;
printf("y = %d\n", y);

x = 0;
printf("x = %d\n", x);

};
return 0;
}