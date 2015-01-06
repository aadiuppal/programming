#include<stdio.h>
#include<string.h>

char * short_str(char *str){
	int count1,count2;
	char *str_new=(char *)malloc(2*strlen(str)*sizeof(char));
	char c;
	int i,j,k=0;
	for(i=0;i<strlen(str);i++){
		c=str[i];
		count1=0;
		for(j=i;j<strlen(str);j++){
			if(str[j]==c){
				count1++;
			}
			else{
				break;
			}
			i=j;
		}
		str_new[k]=c;
		k++;
		if (count1 > 9){
			count2=count1%10;
			count1=count1/10;
			count1=count1+(int)'0';
			str_new[k]=count1;
			k++;
			count2=count2+(int)'0';
			str_new[k]=count2;
			k++;
		}
		else{
			count1=count1+(int)'0';
			str_new[k]=count1;
			k++;
		}
	}
	if (strlen(str_new)<strlen(str)){
		return str_new;
	}
	else{
		return str;
	}
}

int main(){
	char str[]="aaaaaaaaaaaaaaaaaaaaabc";
	char *str1;
	printf("::%s::\n",str);
	str1=short_str(str);
	printf("::%s::\n",str1);
}
