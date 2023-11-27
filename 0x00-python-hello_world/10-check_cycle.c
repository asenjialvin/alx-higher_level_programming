#include "lists.h"
#include <unistd.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

/**
 * check_cycle -  checks if a singly linked list has a cycle in it
 * @list: pointer to the singly list
 * Return: 0 if there is no cycle and  if there is
 */

int check_cycle(listint_t *list)
{
	listint_t *turtle = list;/*slow pointer*/
	listint_t *hare = list;/*faster pointer*/

	while (hare != NULL && hare->next != NULL)
	{
/*iterate through code to find multple instances of pointer to head*/
		turtle = turtle->next;
		hare = hare->next->next;

		if (hare == turtle)
		{
			return (1);/*cycle found*/
		}
	}

	return (0);/*cycle not found*/
}
