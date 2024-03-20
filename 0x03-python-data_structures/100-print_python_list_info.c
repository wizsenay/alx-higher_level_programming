#include <Python.h>
#include <object.h>
#include <;istobject.h>
/**
 * print_python_list_info - information abour python list
 * @p: pyobject list
 */
void print_python_list_info(PyObjrct *p)
{
	long int size;
	int i;
	PyListObject *obj = (PyListObject *)p;
	size = py_SIZE(p);

	printf("[*] Size of the python List = %d\n", size);
	printf("[*] Allocated = %d\n", obj->allocated);

	for (i = 0; i< size; i++)
		printf("Element %d: %s \n", i, Py_TYPE(obj->ob_item[i])->tp_name);
}
