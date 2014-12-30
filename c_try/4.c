#include<stdio.h>

void print_arr(int arr[],int len){
	int i=0;
	for (i=0;i<len;i++){
		printf("::%d::",arr[i]);
	}
	printf("\n");
}

void swap(int *a, int *b){
	int t =*a;
	*a=*b;
	*b=t;

}

int partition(int arr[],int s,int e){
	int x =arr[e];
	int i= s;
	int j;
	for (j=s;j<=e;j++){
		if(arr[j]<=x){
			swap(&arr[i],&arr[j]);
			i++;
		}
	}
	return i-1;
}

void qsort(int arr[],int s,int e){
	int p;
	if (s<e){
		print_arr(arr,10);
		p=partition(arr,s,e);
		qsort(arr,s,p-1);
		qsort(arr,p+1,e);
	}
}

int main(){
	int arr[]={9,10,4,3,7,2,5,12,1,8};
	print_arr(arr,10);
	qsort(arr,0,9);
	print_arr(arr,10);
}
