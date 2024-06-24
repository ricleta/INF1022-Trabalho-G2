#include <stdio.h>
int main() {
int a = 0;
int b = 0;

// int b = 0;

a = 10;b = a;
if (a == 10) 
{
    if (b == a) 
    {
        b = b + 1;
    };
} 
else 
{
    a + 2;
};

printf("%d\n", a);
printf("%d\n", b);
return 0;
}