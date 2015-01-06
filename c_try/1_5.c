#include<stdio.h>
#include<string.h>

char * short_str(char *str){
	int count;
	char *str_new=(char *)malloc(2*strlen(str)*sizeof(char));
	char c;
	int i,j,k=0;
	for(i=0;i<strlen(str);i++){
		c=str[i];
		count=0;
		for(j=i;j<strlen(str);j++){
			if(str[j]==c){
				count++;
			}
			else{
				break;
			}
			i=j;
		}
		str_new[k]=c;
		k++;
		count=count+(int)'0';
		str_new[k]=count;
		k++;
	}
	return str_new;
}

int main(){
	char str[]="aaabbb";
	char *str1;
	printf("::%s::\n",str);
	str1=short_str(str);
	printf("::%s::\n",str1);
}
