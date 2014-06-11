##
##  using descriptor automatically generate __doc__
##

class APIDOC(object):
    def _print_values(self, obj):
        def _print_value(key):
            if key.startswith('_'):
                return ''
            value = getattr(obj, key)
            if not hasattr(value, '__func__'):
                doc = type(value).__name__
            else:
                if value.__doc__ is None:
                    doc = 'no docstring'
                else:
                    doc = value.__doc__
            return ' %s\t-> %s' % (key, doc)
        res = [_print_value(el) for el in dir(obj)]
        return '\n'.join([el for el in res if el != ''])

    def __get__(self, instance, klass):
        if instance is not None:
            return self._print_values(instance)
        else:
            return self._print_values(klass)

class MyClass(object):
    __doc__ = APIDOC()

    def __init__(self):
        self.value = ''

    def getval(self):
        """returns value"""
        return self.value



#test
print(MyClass.__doc__)
#   output:     getval	-> function

instance = MyClass()
print(instance.__doc__)
#   output:     getval	-> returns value
#               value	-> str

