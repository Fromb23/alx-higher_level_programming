#include <Python.h>

void print_python_list_info(PyObject *pList)

{
	if (!PyList_Check(pList)) {
		printf("Error: Object is not a list.\n");
		return;
	}

	Py_ssize_t size = PyList_Size(pList);
	PyObject *pItem;

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", ((PyListObject *)pList)->allocated);

	for (Py_ssize_t i = 0; i < size; i++)
	{
		pItem = PyList_GetItem(pList, i);
		printf("Element %ld: %s\n", i, Py_TYPE(pItem)->tp_name);
	}
}
