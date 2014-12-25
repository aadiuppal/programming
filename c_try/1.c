#include<stdio.h>

struct node{
	int data;
	struct node *next;
};


struct node*  newnode(){
	return (struct node *)malloc(sizeof(struct node));
}

void insert_node(struct node **head,int data){
	struct node *new_node= newnode();
	struct node *last = *head;
	struct node *temp;
	if (last != NULL){
		while(last->next!=NULL){
			last=last->next;
		}
	new_node->data=data;	//TODO
	new_node->next=NULL;
	last->next=new_node;
	}
	else{
		new_node->data=data;	//TODO
		new_node->next=NULL;	
		*head = new_node;
		
	}
}


void insertafter(struct node **head,int data_after,int data){
	struct node *new_node=newnode();
	struct node *trav=*head;
	while(trav->data != data_after){
		trav=trav->next;
	}
	new_node->data=data;
	new_node->next=trav->next;
	trav->next=new_node;
}	

void push(struct node **head,int data){
	struct node *new_node= newnode();
	//if (head == NULL){
		new_node->data=data;
		new_node->next=*head;
		*head=new_node;
//	}
/*	else{
		new_node->data=data;
		new_node->next=*head;
		*head=new_node;
	}*/
}


struct node* delete_node(struct node **head,int data_del){
	struct node *trav=*head;
	struct node *temp;
//	if (*head == NULL){
//	return;
//	}
	if( (trav->next != NULL) && (trav->data != data_del)){
		while(trav->data != data_del){
			temp=trav;
			trav=trav->next;
		}
		temp->next=trav->next;
		free(trav);
	}
	else{
		*head=trav->next;
		free(trav);
	}
	return *head;
}

struct node* pop(struct node **head){
	struct node *temp = *head;
	*head=temp->next;
	//free(temp);
	return *head;
}

void dequeue(struct node **head){
	struct node *temp=*head;
	struct node *prev;
	while(temp->next != NULL){
		prev=temp;
		temp=temp->next;
	}
	prev->next=NULL;
		
}

void enqueue(struct node **head,int data){
	struct node *temp=*head;
	struct node *new_node=newnode();
	new_node->data=data;
	new_node->next=temp;
	*head=new_node;
}


int detectloop(struct node **head){
	struct node *slow=*head;
	struct node *fast=*head;
	while (slow && fast && fast->next ){
		slow=slow->next;
		fast=fast->next->next;
		if (slow == fast){
			return 1;
		}
	}
	return 0;
}

void loopto(struct node **head,int data_loop){
	struct node *temp=*head;
	struct node *trav=*head;
	while (temp->data!=data_loop)	{
		temp=temp->next;
	}
	while(trav->next!=NULL){
		trav=trav->next;
	}
	trav->next=temp;
}

void looptohead(struct node **head){
	struct node *temp=*head;
	struct node *trav=*head;
	while (trav->next != NULL){
		trav=trav->next;
	}
	trav->next=temp;
}

void print_list(struct node *head){
	if (head != NULL){
		while(head!=NULL){
			printf("::%d::",head->data);
			head=head->next;
		}
	}
}

void print_circular_list(struct node **head){
	struct node *start=*head;
	struct node *trav=*head;
	do{
		printf("::%d::",trav->data);
		trav = trav->next;
	}while(trav != start);
}

void print_nth(struct node **head,int index){
	struct node *trav=*head;
	int i;
	for(i=1;i<index;i++){
		trav=trav->next;
	}
	printf("\n at index %d element is %d\n",index,trav->data);
}

int main(){
  /* Start with the empty list */
  struct node* head = NULL;
 
  // Insert 6.  So linked list becomes 6->NULL
  insert_node(&head, 7);
printf("\nloop::%d\n",detectloop(&head));
  // Insert 7 at the beginning. So linked list becomes 7->6->NULL
  insert_node(&head, 8);
 printf("\nloop::%d\n",detectloop(&head));
  // Insert 1 at the beginning. So linked list becomes 1->7->6->NULL
  push(&head, 1);
  push(&head,12);
  insertafter(&head,7,5) ;

//loopto(&head,1); //USE WITH CAUTION
//looptohead(&head);


//printf("\nloop::%d\n",detectloop(&head));
//print_circular_list(&head);
  // Insert 4 at the end. So linked list becomes 1->7->6->4->NULL
  //append(&head, 4);
 
  // Insert 8, after 7. So linked list becomes 1->7->8->6->4->NULL
  insert_node(&head, 81);
  insert_node(&head,9);
  push(&head,123);
  push(&head,321);
  printf("\n Created Linked list is: ");
  print_list(head);
  head=  delete_node(&head,6);
  printf("\n Created Linked list is: ");
  print_list(head);
  head= delete_node(&head,123);
  printf("\n Created Linked list is: ");
  print_list(head);
  pop(&head);
  printf("\n Created Linked list is: ");
  print_list(head);
  pop(&head);
  printf("\n Created Linked list is: ");
  print_list(head);
enqueue(&head,72);
dequeue(&head);
  printf("\n Created Linked list is: ");
  print_list(head);
printf("\nloop::%d\n",detectloop(&head));
print_nth(&head,4);
getchar();
  return 0;
}
