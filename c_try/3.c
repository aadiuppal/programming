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

struct node * min_node(struct node *root){
	if (root->left == NULL){
		return root;
	}
	if (root->left != NULL){
		return min_node(root->left);
	}
}

struct node * max_node(struct node *root){
	if(root->right == NULL){
		return root;
	}
	if (root->right != NULL){
		return max_node(root->right);
	}
}

struct node * delete(struct node *root, int data){
	if (data<root->data){
		root->left=delete(root->left,data);
	}
	else if (data>root->data){
		root->right=delete(root->right,data);
		}
	else{
		if (root->left ==NULL){
			struct node *temp= root->right;
			free(root);
			return temp;
		}
		else if(root->right == NULL){
			struct node *temp= root->left;
			free(root);
			return temp;
		}
		
		struct node *temp = max_node(root->left);
		//struct node *temp = min_node(root->right);

		root->data=temp->data;

		//root->right=delete(root->right,temp->data);
		root->left=delete(root->left,temp->data);
	}
	return root;
}




int main(){
    struct node *root = NULL;
   root= insert_node(root, 50);
    insert_node(root, 30);
    insert_node(root,60);
    insert_node(root,90);
  insert_node(root,55);
	printf("inorder:\n");
    inorder(root);
	printf("\npreorder\n");
    preorder(root);
	printf("\npostorder\n");
    postorder(root);
	printf("search 60\n");
printf(">>%d<<\n",search(root,60)->data);
printf("\ndelete 60\n");
delete(root,60);
	printf("inorder:\n");
    inorder(root);
	printf("\npreorder\n");
    preorder(root);
	printf("\npostorder\n");
    postorder(root);
}
