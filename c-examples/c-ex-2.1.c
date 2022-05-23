
//  Bubblesort
#include <stdio.h>

void bubbleSort(int list[], int shape){
	int i,j;
	for(i=0; i<shape; ++i)
    {
		int in_line=1;
		for (j=0; j <shape-1; ++j)
        {
			if(list[j]>list[j+1])
            {
			    swap(&list[j],  &list[j+1] );
			    in_line=0;
			}
		}
	    if(in_line)
	    break;	
	}
}

void swap (int *num1, int *num2){
	int temp= *num1;
	*num1=*num2;
	*num2=temp;
}

/////////////////////////////
int main()
{
	int i;
    int list[]={64,24,25,12,23,15,50,1};
    int shape= sizeof(list)/sizeof(int);
    
	printf ("%d\n", shape);	
	bubbleSort(list, shape);
	for(i=0; i < shape; ++i)
	    printf ("%d ", list[i]);
}