#include<stdio.h>

 void rot_mat(int arr[][2],int new_arr[][2],int N,char c){
	//int new_arr[N][N];
	int i,j;
	//for (i=0;i<N;i++){
	//	new_arr[i]=(int *)malloc(N*sizeof(int));
	//}
	for (i=0;i<N;i++){
		for (j=0;j<N;j++){
			new_arr[i][N-j-1]=arr[j][i];
	//		printf("%d<-%d\n",new_arr[N-j-1][i],arr[i][j]);
		}
	}
	
//	return new_arr;
}

void print_arr(int arr[][2],int N){
	int i,j;
	for (i=0;i<N;i++){
		for (j=0;j<N;j++){
			printf("%d\t",arr[i][j]);
		}
		printf("\n");
	}
}

void print(int *arr[], int m, int n)
{
    int i, j;
    for (i = 0; i < m; i++)
      for (j = 0; j < n; j++)
        printf("%d ", **((arr+i*n) + j));
}

int main(){
	int new_arr[2][2];
	int arr[2][2]={1,2,3,4};
	print_arr(arr,2);
	//new_arr=
	rot_mat(arr,new_arr,2,'l');
	print_arr(new_arr,2);
	return 0;
}
