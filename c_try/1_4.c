#include<stdio.h>

void str_rep(char *str){
	int count=0;
	int i,j;
	char c;
	static char *temp;
	temp=str;
	while (*str != '\0'){
		count++;
		*str++;
	}
	*str--;
	while(*str == ' '){
		count--;
		*str--;
	}
	for(i=1;i<count;i++){
		*str--;
	}
	for (i=0;i<count;i++){
		if (str[i] == ' '){
			for (j=count+1;j>i;j--){
				str[j]=temp[j-2];
			}
			str[i]='%';
			str[i+1]='2';
			str[i+2]='0';
			i=i+2;
		}
	}
}

int main(){
	char str[]="asd 123  ";
	printf(":%s:\n",str);
	str_rep(str);
	printf(":%s:\n",str);
	return 0;
}
