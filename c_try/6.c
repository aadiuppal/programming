#include<stdio.h>

struct adj_list_node{
	int dest;
	struct adj_list_node *next;
};

struct adj_list{
	struct adj_list_node *head;
};

struct graph{
	int v;
	struct adj_list *array;
};

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

void add_edge(struct graph *graph,int src,int dest){
	struct adj_list_node *new_node=new_adj_list_node(dest);
	new_node->next=graph->array[src].head;
	graph->array[src].head=new_node;

	new_node=new_adj_list_node(src);
	new_node->next=graph->array[dest].head;
	graph->array[dest].head=new_node;
}

void print_graph(struct graph *g){
	int v;
	for (v=0;v<g->v;v++){
		struct adj_list_node *trav=g->array[v].head;
		printf("\nV=%d\n",v);
		while(trav){
			printf("->%d",trav->dest);
			trav=trav->next;
		}
	}
}


int main(){
	int v=5;
	struct graph *g=create_graph(v);
    add_edge(g, 0, 1);
    add_edge(g, 0, 4);
    add_edge(g, 1, 2);
    add_edge(g, 1, 3);
    add_edge(g, 1, 4);
    add_edge(g, 2, 3);
    add_edge(g, 3, 4);
	print_graph(g);
	return 0;
}
