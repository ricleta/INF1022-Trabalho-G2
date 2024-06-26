#include <stdio.h>
int main() {
int X = 0;
int Y = 0;
int L = 0;
int Z = 0;

// Monitored vars =  Z
printf("Z = %d\n", Z);


Z = 0;
printf("Z = %d\n", Z);
X = 5;Y = 0;L = 1;
if (Y != 0) {

for (int i = 0; i < X - L; i++) {
Z = Z * L;
printf("Z = %d\n", Z);

};
} else {

for (int i = 0; i < X - L; i++) {
Z = Z * X;
printf("Z = %d\n", Z);

};
};
return 0;
}