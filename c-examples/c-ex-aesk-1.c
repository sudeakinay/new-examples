#include <stdio.h>
int main()
{
    int a;
    do
    {
        int number, i;
        unsigned long long factorial = 1;
        printf("\n enter a positive numver: ", number);
        scanf("%d", &number);

        if(number <= 0)
        {
            printf("please enter a POSITIVE numver!");
        }
        else
        {
            for(i=1; i<number; ++i)
            {
                factorial *= i;
            }
        }

        printf(" factorial of the number %d is: %llu ", number, factorial);
        printf("\n press 1 to continue \n", a);
        scanf("%d", &a);

    } while (a == 1);

    return 0;
}