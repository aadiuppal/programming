#include<stdio.h>

void reverse(char* str){
  char *temp=str, *temp2;
  char t;
  int len=0;
  int i,j;
  printf("%s\n",temp);
  while (*temp!='\0'){
    temp++;
    len++;
  }
  temp--;
  i=0;
  j=len-1;
  while (i<j){
    t=*str;
    printf("%c,%c<-->%c\n",t,*str,*temp);
    *str=*temp;
    *temp=t;
    str++;
    i++;
    j--;
    temp--;
  }
}

int main(){
  char str[]="string";
  printf("%s\n",str);
  reverse(str);
  printf("%s\n",str);
  return 0;
}
