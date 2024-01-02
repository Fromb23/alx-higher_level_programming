#include "lists.h"
#include <stdlib.h>
#include <stddef.h>

/**
 * insert_node - Inserts a new node in a sorted linked list.
 * @head: Pointer to the head of the linked list.
 * @number: Value to be inserted.
 *
 * Return: Pointer to the newly inserted node, or NULL on failure.
 **/

listint_t *insert_node(listint_t **head, int number)

{
	listint_t *new_node;

	newNode = malloc(sizeof(listint_t));
	if (newNode == NULL)
		return (NULL);

	newNode->n = number;
	newNode->next = NULL;

	if (*head == NULL || number < (*head)->n)
	{
		newNode->next = *head;
		*head = newNode;
	}
	else
	{
		listint_t *current = *head;
		listint_t *previous = NULL;

		while (current != NULL && number > current->n)
		{
			previous = current;
			current = current->next;
		}

		if (previous != NULL)
		{
			previous->next = newNode;
			newNode->next = current;
		}
	}

	return (newNode);
}
