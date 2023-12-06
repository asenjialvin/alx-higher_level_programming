#include <Python.h>

/**
 * print_python_list - prints basic info about python lists
 * @p: pointer to PyObject
 */

void print_python_list(PyObject *p)
{
	PyObject *item;
	Py_ssize_t size, j;

	size = PyList_Size(p);

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	for (j = 0; j < size; j++)
	{
		item = *(p + j);
		printf("Element %ld: %s\n", j, PyObject_Type(item)->tp_name);
	}
}

/**
 * print_python_bytes - print some basic info about Python bytes objects
 * @p: pointer to PyObject
 */

void print_python_bytes(PyObject *p)
{
	char *string;
	Py_ssize_t size, j;

	if (!PyBytes_Check(p))
	{
		printf("[.] bytes object info\n");
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = PyBytes_Size(p);
	string = PyBytes_AsString(p);

	printf("[.] bytes object info\n");
	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", string);
	printf("  first %ld bytes:", (size > 10) ? 10 : size);

	for (j = 0; j < ((size > 10) ? 10 : size); j++)
		printf(" %02x", (unsigned char)string[j]);

	printf("\n");
}
