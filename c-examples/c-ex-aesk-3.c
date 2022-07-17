#include <stdio.h>

void ters(char *string);

int main()
{
    char string [] = "fonksiyon";
    printf("\n  the string at first:   %s\n", string);
    printf("\n  the reverse of string:   ");
    ters(string);

    return 0;
}

void ters(char *string)
{
    int count, end, begin;
    char r[1000];

    while(string[count] != "\0")
        count++;
    end = count - 1;
    for(begin = 0; begin < count; begin++)
    {
        r[begin] = string[end];
        end--;
    }

    r[begin] = "\0";
    printf("%s\n", r);
}