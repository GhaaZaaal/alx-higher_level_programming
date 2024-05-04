#include "lists.h"
/**
 * check_cycle - Function to check if the single list has a cycle
 *
 * @list: pointer to the head of the list
 *
 * Return: 0 if no cycles, 1 if cycles
 */

int check_cycle(listint_t *list)
{
	listint_t *temp = list;

	temp = temp->next;
	while (temp != NULL)
	{
		if (temp == list)
			return (1);
		temp = temp->next;
	}
	return (0);
}
