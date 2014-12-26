#include<stdio.h>

int check_string(char *str){
	char *temp=str;
	while (*str!='\0'){
		*temp++;
		while(*temp!='\0'){
			if (*str == *temp){
				return 1;
			}
			*temp++;
		}
		*str++;
		temp=str;
	}
	return 0;
}

int main (){
	char *str="123ads";
	char *str1="asasd";
	printf("\n:str:%d:str1:%d::\n",check_string(str),check_string(str1));
	return 0;
}
