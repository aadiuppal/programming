#include<stdio.h>
#include<string.h>

char *rev_str(char *str){
	char *temp= (char *)malloc(sizeof(char)*strlen(str));
	*temp=*temp+(strlen(str)*sizeof(char));
	*temp='\0';
	while(*str!='\0'){
		*temp--;
		*temp=*str;
		*str++;
	}
	return temp;
}

int main(){
	char *str="123asd";
	printf("::%s::\n",rev_str(str));
}
