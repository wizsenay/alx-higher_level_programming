#include <python.h>
/**
 * print_python_list_info - information abour python list
 * @p: pyobject list
 */
void print_python_list_info(PyObjrct *p)
{
	int size, alloc, i;
	PyObject *obj;

	size = py_SIZE(p);
	alloc = ((PyObject *)p)->allocated:

	printf("[*] Size of the python List = %d\n", size);
	printf("[*] Allocated = %d\n", alloc);

	for (i = 0; i< size; i++)
	{
		printf("Element %d: ", i);
		obj = PyList_GetUtem(p, i);
		printf("%s\n", Py_TYPE(obj)->tp_name);
	}
}
