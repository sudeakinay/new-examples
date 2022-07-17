#include <stdio.h>
int main()
{
    int n, i, j, temp;
    int array[5] = {1, 2, 3, 4, 5};
    printf("the array at first:");

    for (i=0; i<5; i++ )
    {
        printf("%d  ", array[i]);
    }

    printf("\n how many times do you want the array to be shifted aside?");
    scanf("%d", &n);

    for (i=0; i<n; i++)
    {
        temp = array[0];
        for(j=0; j<4; j=j+1 )
        {
            array[j] = array[j+1];
        }
        array[4] = temp;
    }

    for (i=0; i<5; i++)
    {
        printf("%d   ", array[i]);
    }
    
    return 0;
}