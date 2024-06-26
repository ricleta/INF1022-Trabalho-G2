#include <stdio.h>
int main() {
int X = 0;
int Y = 0;
int Z = 0;

// Monitored vars =  Z
printf("Z = %d\n", Z);

Y = 2;X = 5;Z = Y;
printf("Z = %d\n", Z);
while (X != 0) {
Z = Z + 1;
printf("Z = %d\n", Z);
X = X - 1;
};
return 0;
}