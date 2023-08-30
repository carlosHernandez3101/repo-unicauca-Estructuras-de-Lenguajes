#include <stdio.h>
#include <stdlib.h>

int main(){
	
	int y, j, t, *np, *mp;
	float *pt;
	
	y = 12;
	j = 20;
	np = &j;
	*np = 35;
	y = *np - 15;
	mp = np;
	t = *np + *mp;
	pt = &t;
	
	printf("%d\n", y);
	
	return 0;
}