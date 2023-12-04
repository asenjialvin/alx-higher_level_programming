#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

listint_t *reverse_list(listint_t *head);

/**
 * is_palindrome - checks if function is palindrome
 * @head: pointer to the head
 * Return: 1 if palindrome, 0 otherwise
 */

int is_palindrome(listint_t **head)
{
	listint_t *fast_node = *head, *slow_node = *head;
	listint_t *second_half, *p1, *p2;

	if (*head == NULL) /*empty list*/
		return (1);

	/*slow_node will be at middle when fast_nodeis at end of list*/
	/*find middle of list*/
	while (fast_node->next != NULL && fast_node->next->next != NULL)
	{
		slow_node = slow_node->next;
		fast_node = fast_node->next->next;
	}

	/*reverse the list*/
	second_half = reverse_list(slow_node->next);

	/*compare both halves*/
	p1 = *head;
	p2 = second_half;
	while (p2 != NULL)
	{
		if (p1->n != p2->n)
		{
			reverse_list(second_half);
			return (0);
		}
		p1 = p1->next;
		p2 = p2->next;
	}
	/*set list back to normal*/
	reverse_list(second_half);
	return (1);
}

/**
 * reverse_list - reverses the linked listint_t
 * @head: pointer to the address of the first node
 * Return: pointer to previous_node
 */

listint_t *reverse_list(listint_t *head)
{
	listint_t *previous_node = NULL;
	listint_t *current_node = head;
	listint_t *next = NULL;

	while (current_node != NULL)
	{
		next = current_node->next;
		current_node->next = previous_node;
		previous_node = current_node;
		current_node = next;
	}
	return (previous_node);
}
