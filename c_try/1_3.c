#include<stdio.h>

void swap(char *str1,char *str2){
	char t=*str1;
	*str1=*str2;
	*str2=t;
}

int partition(char str[],int s,int e){
	int j,i=s;
	char x =str[e];
	if (s<e){
		for (j=s;j<=e;j++){
			if(str[j]<=x){
				swap(&str[j],&str[i]);
				i++;
			}
		}
	}
	return i-1;
}

void qsort(char str[],int s, int e){
	int p;
	if (s<e){
		p=partition(str,s,e);
		qsort(str,s,p-1);
		qsort(str,p+1,e);
	}
}

int is_permute(char *str1,char *str2){
	int i;
	qsort(str1,0,5);
	qsort(str2,0,5);
	for(i=0;i<5;i++){
		if (str1[i] != str2[i]){
			return 0;
		}
	}
	return 1;
}

int main(){
	char str1[]="qweas";
	char str2[]="wqaes";
	char str3[]="aaass";
	printf("<:%s<:%s<:%s\n",str1,str2,str3);
	printf("<:%d<:%d<:%d\n",is_permute(str1,str2),is_permute(str2,str3),is_permute(str3,str1));
}
