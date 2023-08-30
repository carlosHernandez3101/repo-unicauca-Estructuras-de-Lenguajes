#include <stdio.h>
#include <stdlib.h>

void sumar(int x, int y, int *z);

int main(){
	
	int x, y, z;
	
	x = 15;
	y = 25;
	
	sumar(x, y, &z);
	
	printf("%d\n", z);
	return 0;
}

void sumar(int x, int y, int *z){
	*z = x + y;
}