
//	FIND REPEATING LETTERS

#include <stdio.h>
int main () 
{
	static int counter[26];
	int i, j, index, total=0, normal;	
	char sentence[100];	          
	printf("enter a sentence without spaces:  ");
	scanf("%s", sentence);	
	i=0;	
	while(sentence[i] != 0)
	{
		if((sentence[i] <= 'z') && (sentence[i] > 'a'))		//if lowercase
		{
			index = sentence[i] - 'a';						// find out how many letters it is
			sentence[index]++;								// increase the corresponding index
		}
	i++;	
	}	
	for(i = 0; i < 26; i++)
	{
		printf( "%c : %d \n ", 'a'+ i , counter[i]); 		//how many times all letters are repeated is printed
	}	
	//but it doesn't print the letters a? I dont know the reason.	
	return 0;
}

