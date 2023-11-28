#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
#include <string.h>

/**
 * insert_node - inserts node in ascending order i a sorted list
 * @head: pointer to the first node
 * @number: value of the node to insert
 * Return: pointer to address of new node or NULL
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node, *current;
	/*create memory for new node*/
	new_node = malloc(sizeof(listint_t));

	if (new_node == NULL)
		return (NULL);

	new_node->n = number;
	new_node->next = NULL; /*for now*/

	 /* iterate through list to find where number should be inserted */
	if (*head == NULL || number < (*head)->n)/*empty list*/
	{
		new_node->next = *head;
		*head = new_node;
		return (new_node);
	}

	current = *head;
	while (current->next != NULL && current->next->n < number)
		current = current->next;

	/* insert number by making the previous node point towards number*/
	new_node->next = current->next;
	current->next = new_node;

	return (new_node->next);
}
