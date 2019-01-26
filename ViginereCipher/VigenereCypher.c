//#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char* argv[])
{    
    // Check if correct # of arguments given
    if (argc != 2)
    {
        printf("Wrong number of arguments. Please try again.\n");

        return 1;
    }
    else 
    {
        for (int i = 0, n = strlen(argv[1]); i < n; i++)
        {
            if (!isalpha(argv[1][i]))
            {
                printf("Key must be alphabetic chars only.");

                return 1;
            }    
        }
    }

     printf ("plaintext:");
     
    // Store key as string and get length
    char k [100];
	
	for (int i =0;i <strlen(argv[1]);i++)
	{
		k[i]=argv[1][i];
	}
    int kLen = strlen(k);

    // Get text to encode
    char p [100];
	//string p = GetString();
	 scanf("%[^\n]s",p);
    
    printf("ciphertext: ");
    // Loop through text
    for (int i = 0, j = 0, n = strlen(p); i < n; i++)
    {            
        // Get key for this letter
        int letterKey = tolower(k[j % kLen]) - 'a';

        // Keep case of letter
        if (isupper(p[i]))
        {
            // Get modulo number and add to appropriate case
            printf("%c", 'A' + (p[i] - 'A' + letterKey) % 26);

            // Only increment j when used
            j++;
        }
        else if (islower(p[i]))
        {
            printf("%c", 'a' + (p[i] - 'a' + letterKey) % 26);
            j++;
        }
        else
        {
            // return unchanged
            printf("%c", p[i]);
        }
    }
    printf("\0");
    printf("\n");

    

    return 0;
} 
