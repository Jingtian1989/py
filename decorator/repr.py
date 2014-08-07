#case 1
def __myrepr__(obj):
    def _print_value(key):
        if key.startswith('_'):
                return ''
        value = getattr(obj, key)
        if not hasattr(value, '__func__'):
            return '%s:%s' % (key, value)
    res = [_print_value(el) for el in dir(obj)]
    res = ','.join([el for el in res if el != ''])
    return "{" + res + "}"

def setrepr(klass):
    setattr(klass, '__repr__', __myrepr__)
    return klass

@setrepr
class Brand(object):
    def __init__(self, name):
        self.name = name

@setrepr
class Car(object):
    def __init__(self, owner, brand):
        self.owner = owner
        self.brand = Brand(brand)

obj1 = Car('coly', 'jetta')
obj2 = Car('coly', 'volo')
print(obj1)
print(obj2)
print([obj1, obj2])


#case 2
class MyRepr(object):
    def _print_values(self, obj):
        def _print_value(key):
            if key.startswith('_'):
                return ''
            value = getattr(obj, key)
            if not hasattr(value, '__func__'):
                if hasattr(value, '__myrepr__'):
                    value = value.__myrepr__
                return '%s:%s' % (key, value)
        res = [_print_value(el) for el in dir(obj)]
        return ','.join([el for el in res if el != ''])

    def __get__(self, instance, klass):
        if instance is not None:
            return "{" + self._print_values(instance) + "}"
        return ''
class Driver(object):
    __myrepr__ = MyRepr()
    def __init__(self, name):
        self.name = name

driver = Driver('coly')
print(driver.__REPR__)
