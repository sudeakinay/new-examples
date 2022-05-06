
//	THE SLOPE OF A LINE WITH KNOWN X-Y COORDINATES

#include <stdio.h>
int main ()
{
	float dx1, dy1, dx2, dy2, slope; // x-y coordinates and the slope 
	printf("x and y value of the first point where the line passes:  ");
	scanf("%f %f ", &dx1, &dy1);	
	printf("\nx and y value of the second point where the line passes:  ");
	scanf("%f %f ", &dx2, &dy2);	
	slope = (dy2-dy1) / (dx2-dx1);	
	printf( "\nslope is: %f ", slope);	
	return 0;
}
