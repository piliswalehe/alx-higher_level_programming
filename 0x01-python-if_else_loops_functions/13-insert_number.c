#include "lists.h"
#include <stdlib.h>
#include <stdio.h>
#include <stddef.h>

/**
 * insert_node - inserts a new node
 * at a given position.
 * @head: head of a list.
 * @number: index of the list where the new node is
 * added.
 * Return: the address of the new node, or NULL if it
 * failed.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *a;
	listint_t *a_prev;

	a = *head;
	new = malloc(sizeof(listint_t));

	if (new == NULL)
		return (NULL);

	while (a != NULL)
	{
		if (a->n > number)
			break;
		a_prev = a;
		a = a->next;
	}

	new->n = number;

	if (*head == NULL)
	{
		new->next = NULL;
		*head = new;
	}
	else
	{
		new->next = a;
		if (a == *head)
			*head = new;
		else
			a_prev->next = new;
	}

	return (new);
}
