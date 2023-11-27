#include "lists.h"

/**
 * check_cycle - checks if linked list has a cycle
 * @list: pointer to list
 * Return: 0 if no cycle and 1 if cycle is present
 */
int check_cycle(listint_t *list)
{
	listint_t *head1 = list;
	listint_t *head2 = list;

	while (head1 != NULL && head2 != NULL && head2->next != NULL)
	{
		head1 = head1->next;
		head2 = head2->next->next;

		if (head1 == head2)
		{
			return (1);
		}
	}
	return (0);
}
