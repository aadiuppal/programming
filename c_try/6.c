#include<stdio.h>

struct adj_list_node{
	int dest;
	struct adj_list_node *next;
}

struct adj_list{
	struct adj_list_node *head;
}

struct graph{
	int V;
	struct adj_list *array;
}

struct adj_list_node * new_adj_list_node(int dest){
	struct adj_list_node *new_node= (struct adj_list_node *)malloc(sizeof(struct adj_list_node));
	new_node->dest=dest;
	new_node->next=NULL;
	return new_node;
}

struct graph * create_graph(int v){
	struct graph *new_graph=(struct graph *)malloc(sizeof(struct graph));
	new_graph->v=v;
	new_graph->array= (struct adj_list *)malloc(v*sizeof(struct adj_list));
	int i;
	for(i=0;i<v;i++){
	new_graph->array[i].head=NULL;
	}
	return new_graph;
}

void add_edge(struct * graph,int src,int dest){
	struct adj_list_node *new_node=new_adj_list_node(dest);
	new_node->next=graph.array[src].head;
	graph->array[src].head=new_node;

	new_node=new_adj_list(src);
	new_node->next=graph.array[dest].head;
	graph->array[dest].head=new_node;
}
