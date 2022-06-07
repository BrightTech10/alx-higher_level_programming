#include <stdio.h>
#include <python.h>

/**
 * print_python_list_info - prints some basic info about Pyhton lists
 * @p: Python list object
 */
void print_python_list_info(PyObject *p)
{
	int list_size, count, num_alloc;
	PyObject *obj;

	list_size = PyList_Size(p); /* Number of list items */
	/* Numbers of accommodable list items */
	num_alloc = sizeof((PyListObject *) p)->allocated;

	printf("[*] Size of the Python List = %d\n", list_size);
	printf("[*] Allocated = %d\n", num_alloc)

	for (count = 0; count < list_size; count++)
	{
		printf("Element %d: ", i);
		obj = PyList_GetItem(p, i); /* Gets object at index i in the list p */
		printf("%s\n", Py_TYPE(obj)->tp_name);
	}
}
