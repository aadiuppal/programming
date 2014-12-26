#include<stdio.h>

struct node{
	int data;
	struct node *next;
	struct node *prev;
};

struct node* newnode(){
	return (struct node *)malloc(sizeof(struct node));
}

void insert_node(struct node **head,int data){
	struct node *new_node=newnode();
	struct node *trav=*head;
	new_node->data=data;

	if (*head == NULL){
		new_node->next=NULL;
		new_node->prev=NULL;
		*head=new_node;
	}
	else{
		while(trav->next!=NULL){
			trav=trav->next;
		}
		new_node->next=NULL;
		new_node->prev=trav;
		trav->next=new_node;
	}
}

void print_list(struct node **head){
	struct node *trav=*head;
	while(trav!=NULL){
		printf("::%d::",trav->data);
		trav=trav->next;
	}
}

int main(){
	struct node *head=NULL;
	insert_node(&head,1);
	print_list(&head);
	insert_node(&head,2);
	print_list(&head);
	//getch();
	return 0;
}
