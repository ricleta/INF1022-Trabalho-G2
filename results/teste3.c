#include <stdio.h>
int main() {
int counter = 0;
int result = 0;

// Monitored vars =  result
printf("result = %d\n", result);

counter = 0;while (counter < 5) {
result = result + counter;
printf("result = %d\n", result);
counter = counter + 1;
};
return 0;
}