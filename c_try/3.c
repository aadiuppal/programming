#include<stdio.h>

struct node{
	int data;
	struct node *left;
	struct node *right;
};

struct node* newnode(){
	return (struct node *)malloc(sizeof(struct node));
}

struct node* insert_node(struct node *root,int data){
//	struct node *trav=root;

	if (root == NULL){
		struct node *new_node=newnode();
		new_node->data=data;
		new_node->left=NULL;
		new_node->right=NULL;
		root=new_node;
//		return root;
	}
	else if (root->data > data){
		root->left=insert_node(root->left,data);
	}
	else {
		root->right=insert_node(root->right,data);
	}
	return root;
}

struct node * search(struct node *root,int data){
	if (root==NULL || root->data==data){
		return root;
	}
	if (data<root->data){
		return search(root->left,data);
	}
	if (data>root->data){
		return search(root->right,data);
	}
}

void inorder(struct node *root){
	if (root!=NULL){
		inorder(root->left);
		printf("::%d::",root->data);
		inorder(root->right);
	}
}

void preorder(struct node *root){
	if (root!=NULL){
	printf("::%d::",root->data);
	preorder(root->left);
	preorder(root->right);
	}
}

void postorder(struct node *root){
	if (root!=NULL){
		postorder(root->left);
		postorder(root->right);
		printf("::%d::",root->data);
	}
}

int main(){
    struct node *root = NULL;
   root= insert_node(root, 50);
    insert_node(root, 30);
    insert_node(root,60);
    inorder(root);
	printf("\n");
    preorder(root);
	printf("\n");
    postorder(root);
	printf("\n");
printf(">>%d<<\n",search(root,60)->data);
}
