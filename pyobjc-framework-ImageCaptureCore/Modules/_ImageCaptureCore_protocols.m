/*
 * This file is generated by objective.metadata
 *
 * Last update: Mon Dec 28 12:49:50 2015
 */

static void __attribute__((__used__)) use_protocols(void)
{
    PyObject* p __attribute__((__unused__));
#if PyObjC_BUILD_RELEASE >= 1006
    p = PyObjC_IdToPython(@protocol(ICCameraDeviceDelegate)); Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(ICDeviceBrowserDelegate)); Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(ICDeviceDelegate)); Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(ICScannerDeviceDelegate)); Py_XDECREF(p);
#endif
#if PyObjC_BUILD_RELEASE >= 1007
    p = PyObjC_IdToPython(@protocol(ICCameraDeviceDownloadDelegate)); Py_XDECREF(p);
#endif
}
