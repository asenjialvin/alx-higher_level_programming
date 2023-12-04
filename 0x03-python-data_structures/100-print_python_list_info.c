#include <Python.h>

/**
 * print_python_list_info - prints basic info about python
 * @p: pointer to PyObject
 */

void print_python_list_info(PyObject *p)
{
	int size, allocation, i;
	PyObject *object;

	size = Py_SIZE(p);
	allocation = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", allocation);

	i = 0;
	while (i < size)
	{
		printf("Element %d: ", i);

		object = PyList_GetItem(p, i);
		printf("%s\n", Py_TYPE(object)->tp_name);
		i++;
	}
}
