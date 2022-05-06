
/*	PROBLEM:
	Write a program to find the value of cos(x) for the given number of terms n and x!
		Without using ready-made functions for reason finding and factorial calculation
		Let's find the necessary information for each term by subtracting it from the previous one.
*/ 

#include <stdio.h>
int main ()
{
	int n, x, i, divisor, dividend, flag;
	float cosx;
	printf("enter the number of terms and x:  ");
	scanf("%d %d", &n, &x);
	divisor =1;
	dividend=1;
	flag=1;
	cosx = 1;	
	for (i=1; i < n ; i++)
	{
		dividend = dividend * x *x;
		divisor = divisor * (2*i) * (2*i-1); // 1 * 2 *1; 2*4*3; 4!*6*5; 6!*8*7;
		flag =-flag;
		cosx=cosx+flag * ((float) dividend/divisor);
	}	
	printf("%f ", cosx);
	return 0;
}
