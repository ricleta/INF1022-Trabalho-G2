#include <stdio.h>
int main() {
int X = 0;
int Y = 0;
int B = 0;
int Z = 0;

// Monitored vars =  Z
printf("Z = %d\n", Z);

X = 5;Y = 2;B = 0;
for (int i = 0; i < X - Y; i++) {

if (B != 0) {
Z = Z + 2;
printf("Z = %d\n", Z);

} else {
Z = Z + 1;
printf("Z = %d\n", Z);

};
};
return 0;
}