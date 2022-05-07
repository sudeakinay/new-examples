
//	FINDING THE ROOTS OF AN EQUATION WITH 2 UNKNOWNS

#include <stdio.h>
#include <math.h>
int main ()
{
	int a, b, c, delta;
	float x1, x2;	
	printf("Enter the coefficients of the function with 2 unknowns: " );
	scanf("%d %d %d ", &a, &b, &c);
	printf("\na: %d b:%d c:%d " ,a, b, c);
	delta = b*b - ((4*a) * c );	
	printf("\n delta: %d ", delta);	
	if(delta > 0)
	{
		x1 = (float) (-b +sqrt(delta)) / 2*a;
		x2 = (float) (-b -sqrt(delta)) / 2*a;
		printf("\nroot1: %f, root2: %f ", x1, x2);
		
	}
	else
	{
		if(delta == 0)
		{
			x1 = (float)(-b / 2*a);
			printf("\nThere is a double root and this root: %f", x1 );
		}
			
			printf("\nthere is NOT reel root! ");

	}	
	return 0;
}
