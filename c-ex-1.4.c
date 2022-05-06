
/*	STARS IN SEQUENCE 
	*
	**
	***
	****
	*****
	******
	and so on...
*/

#include <stdio.h>
int main() 
{
	int i, j, line;	
	printf("enter the number of lines:  ");
	scanf("%d", &line);	
	for(i = 1; i <= line; i++) // i < line+1
	{
		for(j = 1; j <= i; j++)
		{
			printf("*");
		}		
		printf("\n");
	}	
	/*
	to print in reverse;		
	for(i = line; i >= 1; i--) // i < line+1
	{
		for(j = 1; j <= i; j++)
		{
			printf("*");
		}		
		printf("\n");
	}										*/	
	return 0;
}

