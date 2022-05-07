
//	FIND TENS AND ONES DIGIT VALUES

#include <stdio.h>
int main ()
{	
	int number, tens, ones;
	printf(" enter a 2 digit number: " );
	scanf("%d", &number);	
	tens = number/10;
	ones = number -(10*tens),	
	/*
		or 
		ones = number%10;
		tens = (number-ones) / 10;
	*/	
	printf("\nThe tens digit of this number is: %d and ones digit is: %d dir ", tens, ones);
	return 0;
}
