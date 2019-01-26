#include  <stdio.h>  
#include  <ctype.h>  
#include  <string.h> 
#include  <stdlib.h> 


#define     MAX			80 
#define     CORRECT_INPUT	2  

int arg_check(int argcount);
void cipher(char *key);
int alpha_check(char *string[]);

int main(int argc, char *argv[])
{
	if (arg_check(argc) == 1)
		return 1; /* exit */
	if (alpha_check(argv) == 2)
		return 2; /* exit */
	char *key = argv[1];

    printf("Enter text");
    printf("ciphertext: ");
	cipher(key);

	return 0;
}


int arg_check(int argcount)
{
	if (argcount != CORRECT_INPUT) {
		printf("Two arguments is the requirement"
		       " to run this application.\n");
		return 1; /* exit */
	}
	return 0;
}

int alpha_check(char *string[])
{
	int len = strlen(string[1]);

	for (int i = 0; i < len; i++) {
		if (!isalpha(string[1][i])) {
			printf("The keyword must consist of"
			       " alphabetical characters.\n");
			return 2;
		}
	}
	return 0;
}


void cipher(char *key)
{
	char text[MAX];
	fgets(text, sizeof(text), stdin);
	int j = 0;

	for (int i = 0; i < strlen(text); i++) {
		j = j % strlen(key);
		if (isupper(text[i])) { /* if text char is upper	*/
			if (isupper(key[j])) { /* if key char is upper	*/
				char upper = (((text[i] - 'A') + (key[j] - 'A')) % 26) + 'A';
				printf("%c", upper);
				//printf("%d\t%c\t%c\t%d\n",j, key[j], upper, upper);
				j++;
			}
		}
		else if (isupper(text[i])) {
			if (islower(key[j])) { /* if key char is upper	*/
				char lower = (((text[i] - 'a') + (key[j] - 'a')) % 26) + 'a';
				printf("%c", lower);
				//printf("%d\t%c\t%c\t%d\n",j, key[j], upper, upper);
				j++;
			}
		}
		else if (islower(text[i])) {
			if (isupper(key[j])) { /* if key char is upper	*/
				char upper = (((text[i] - 'A') + (key[j] - 'A')) % 26) + 'A';
				printf("%c", upper);
				//printf("%d\t%c\t%c\t%d\n",j, key[j], upper, upper);
				j++;
			}
		}
		else if (islower(text[i])) {
			if (islower(key[j])) { /* if key char is upper	*/
				char lower = (((text[i] - 'a') + (key[j] - 'a')) % 26) + 'a';
				printf("%c", lower);
				//printf("%d\t%c\t%c\t%d\n",j, key[j], upper, upper);
				j++;
			}
		}
		else
			printf("%c", text[i]);
	}

	printf("\n");	
}
