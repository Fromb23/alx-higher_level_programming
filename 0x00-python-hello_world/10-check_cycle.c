#include "lists.h"

/**
 * check_cycle - Checks if a linked list has a cycle.
 * @list: A pointer to the head of the linked list.
 *
 * Return: 1 if there is a cycle, 0 otherwise.
 **/

int check_cycle(listint_t *list)

{
	listint_t *new_node, *prev_node;

	new_node = list;
	prev_node = list;
	while (new_node != NULL && new_node->next != NULL)
	{
		prev_node = prev_node->next;
		new_node = new_node->next->next;
		if (prev_node == new_node)
			return (1);
	}
	return (0);
}
