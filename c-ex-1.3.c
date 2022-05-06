
//	PRIME NUMBER FINDER

#include <stdio.h>
int main () 
{
	int n, i, flag=0;
	printf( "enter a positive number:  "  );
	scanf("%d", &n);
	for(i=2; i <= n/2; i++)
	{
		//	prime condition
		if(n % i == 0)
		{
			flag = 1;
			break;
		}
	}	
	if(n  == 1)
	{
		printf( "It is not possible to comment on the primality of the number 1");
	}
	else
	{
		if(flag == 0)
		{
			printf( " \n %d is a prime number." , n);
		}
		else
		{
			printf( "\n%d is NOT a prime number.", n);
		}
	}
	return 0;
}
