#include <stdio.h>
#include <stdlib.h>

int main(){
	int x, *p;
	x = 1;
	p = &x;
	printf("%d\n", x);
	printf("%d\n", &x);
	printf("%d\n", p);
	printf("%d\n", *p);
	printf("%d\n", &p);
	return 0;
}