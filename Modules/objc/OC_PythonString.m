#import "OC_PythonString.h"

@implementation OC_PythonString 

+ newWithPythonObject:(PyObject*)v;
{
	OC_PythonString* res;

	res = [[OC_PythonString alloc] initWithPythonObject:v];
	[res autorelease];
	return res;
}

- initWithPythonObject:(PyObject*)v;
{
	Py_INCREF(v);
	Py_XDECREF(value);
	value = v;
	return self;
}

-(PyObject*)__pyobjc_PythonObject__
{
	Py_INCREF(value);
	return value;
}

-(void)dealloc
{
	PyObjC_BEGIN_WITH_GIL
		PyObjC_UnregisterObjCProxy(value, self);
		[realObject release];
		Py_XDECREF(value);
	PyObjC_END_WITH_GIL

	[super dealloc];
}

-(id)__realObject__
{
	if (!realObject) {
		realObject = [[NSString alloc]
			initWithBytesNoCopy:PyString_AS_STRING(value)
						 length:(unsigned)PyString_GET_SIZE(value)
					   encoding:[NSString defaultCStringEncoding]
				   freeWhenDone:NO];
	}
	return realObject;
}

-(unsigned)length
{
	return [((NSString *)[self __realObject__]) length];
}

-(unichar)characterAtIndex:(unsigned)anIndex
{
	return [((NSString *)[self __realObject__]) characterAtIndex:anIndex];
}

-(void)getCharacters:(unichar *)buffer range:(NSRange)aRange
{
	[((NSString *)[self __realObject__]) getCharacters:buffer range:aRange];
}

@end /* implementation OC_PythonString */