
// FIND THE BIGGEST OF 3 DIFFERENT NUMBERS

#include <stdio.h>
int main () 
{	
	int number1, number2, number3, big;
	printf("give 3 different number \n" );
	scanf("%d %d %d", &number1, &number2, &number3);	
	if(number1<number2 )
	{
		if(number3<number2)
		big = number2;
		else
		big = number3;
	}
	else 
	{
		if(number3 > number1)
		{	
			if(number3 > number2)
			big = number3;
			else 
			big = number2;		
		}
		else
			if(number3 > number2)
			big = number3;
			else
			big = number1;	
	}
	printf("the biggest number among these 3 is = %d", big );
	return 0;

/*
	18. satirdan itibaren bunu yazarsak daha verimli olur
	if(number1 > number3 )
	big = number1;
	else
	big = number3; */
}
