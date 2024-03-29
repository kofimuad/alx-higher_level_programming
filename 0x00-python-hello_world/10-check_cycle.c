#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - Checks if a singly-linked list contains a cycle.
 * @list: A singly-linked list.
 *
 * Return: If there is no cycle - 0.
 *         If there is a cycle - 1.
 */
int check_cycle(listint_t *list)
{
	listint_t *kofi, *ama;

	if (list == NULL || list->next == NULL)
		return (0);

	kofi = list->next;
	ama = list->next->next;

	while (kofi && ama && ama->next)
	{
		if (kofi == ama)
			return (1);

		kofi = kofi->next;
		ama = ama->next->next;
	}

	return (0);
}
