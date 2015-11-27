#include<iostream>
#include <cstddef>
#include<queue>
#include<vector>
using namespace std;
struct node{
  int val;
  node *left = NULL;
  node *right = NULL;
};

class Tree{
  public:
    Tree(){
      this->root = NULL;
    }
    Tree(node *root){
      this->root = root;
    }
  public:
    node *root;
    void insert(int val);
    void print_inorder();
    void _inorder_(node *root);
};

void Tree::insert(int val){
  if (this->root == NULL){
    node *temp = new node;
    temp->val= val;
    this->root = temp;
  }
  else{
    queue<node*> qu;
    qu.push(this->root);
    while (qu.size() > 0){
      node *temp = qu.front();
      qu.pop();
       if (temp->left == NULL){
        temp->left = new node;
        temp->left->val = val;
        break;
       }
       else if (temp->right == NULL){
         temp->right = new node;
         temp->right->val = val;
         break;
       }
      qu.push(temp->left);
      qu.push(temp->right);
    }
  }
}
void Tree::print_inorder(){
  _inorder_(this->root);
  cout<<"\n";
}

void Tree::_inorder_(node *temp){
  if (temp == NULL){
    return;
  }
  _inorder_(temp->left);
  cout<<temp->val<<" ";
  _inorder_(temp->right);
}


int get_maxDepth_Tree(node *root){
  if (root == NULL){
    return 0;
  }
  return 1+ max(get_maxDepth_Tree(root->left),get_maxDepth_Tree(root->left));

}
int get_maxDepth_Tree_BFS(node *root){
  if (root == NULL){
    return 0;
  }
  queue<node*> bfs_qu;
  queue<int> bfs_lev;
  bfs_qu.push(root);
  bfs_lev.push(1);
  node *temp;
  int lev;
  while (bfs_qu.size() > 0){
    temp = bfs_qu.front();
    lev = bfs_lev.front();
    bfs_qu.pop();
    bfs_lev.pop();
    if (temp->left != NULL){
      bfs_qu.push(temp->left);
      bfs_lev.push(lev+1);
    }
    if (temp->right != NULL){
      bfs_qu.push(temp->right);
      bfs_lev.push(lev+1);
    }
  }
  return lev;
}
int main(){
  Tree t;
  for (int i =1; i<= 15;i++){
    t.insert(i);
  }
  t.print_inorder();
  cout<<"max depth = "<<get_maxDepth_Tree((&t)->root)<<"\n";
  cout<<"max depth = "<<get_maxDepth_Tree_BFS(t.root)<<"\n";
  return 0;
}

