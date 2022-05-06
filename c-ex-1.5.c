
//	FIND THE AVERAGE GRADE OF THE STUDENTS

#include <stdio.h>
int main () 
{
	int n, i, st1, st2, total = 0;
	float max = 0, max2 = 0;
	float student[50];	
	do
	{
		printf( "enter the total number of the students:  ");
		scanf("%d ", &n);	
	}
	while (n > 50);	
		for(i = 0; i <n; i++)
		{
			printf("\nenter the grades of %d:", i);
			scanf("%f",  &student[i]);			
			total += student[i];
			if(max < student[i])
			{
				max2 = max;
				st2 = st1;
				max = student[i];
				st1 = i;
			}
			else if(max2 < student[i])
			{
				max2 = student[i];
				st2 = i;
			}		
		}		
		printf("\nthe average grade of the students: %f  highest 1st and 2nd grade is: %f and %f \n is belongs to the: %d and %d students ", total/n, max, max2, st1, st2);		
	return 0;
}

